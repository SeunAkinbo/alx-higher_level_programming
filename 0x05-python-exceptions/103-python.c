#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints the python list information
 * @p: Python Object
 * Return: void
 **/

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);
		printf("Element %zd: ", i);
		PyObject_Print(element, stdout, 0);
		printf("\n");
	}
}

/**
 * print_python_bytes - Prints the python Bytes Information
 * @p: Python Object
 * Return: void
 **/

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	printf("  trying string: ");
	PyObject_Print(p, stdout, Py_PRINT_RAW);
	printf("\n");

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < 10 && i < size; ++i)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints the python Float Information
 * @p: Python Object
 * Return: void
 **/

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
