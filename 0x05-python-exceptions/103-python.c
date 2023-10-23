#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	printf("  [*] Size of the Python List = %ld\n", size);
	printf("  [*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("  Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(p);

	fflush(stdout);

	printf("[.] bytes object info\n");
	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", bytes->ob_sval);

	/*Adjust size to print up to the null terminator*/
	size = (size >= 6) ? 6 : size + 1;

	printf("  [.] first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		printf((i == size - 1) ? "\n" : " ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(PyFloat_AS_DOUBLE(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	fflush(stdout);

	printf("[.] float object info\n");
	printf("  [.] value: %s\n", buffer);

	PyMem_Free(buffer);
}
