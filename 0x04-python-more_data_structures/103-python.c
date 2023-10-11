#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	data = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  [*] Size of the Python Bytes = %zd\n", size);
	printf("  [.*] Bytes: ");

	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02hhx", data[i]);
		if (i < size - 1 && i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}

int main(void)
{
	Py_Initialize();

	/*Example Usage:*/
	PyObject *list = PyList_New(0);  /*Create an empty list*/
	PyList_Append(list, PyLong_FromLong(98));
	PyList_Append(list, PyLong_FromLong(23));
	PyList_Append(list, PyLong_FromLong(34));

	PyObject *bytes = PyBytes_FromString("Hello, Python!");

	print_python_list(list);
	print_python_bytes(bytes);

	Py_DECREF(list);
	Py_DECREF(bytes);

	Py_Finalize();

	return (0);
}
