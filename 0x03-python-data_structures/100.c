#include <Python.h>

/**
 * print_python_list_info - Prints python list
 * @p: Python Object
 **/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	PyObject *item, *repr;
	const char *elementStr;

	if (!PyList_Check(p))
		printf("Error: The provided object is not a Python list\n");

	size = PyList_Size(p);
	printf("List Information:\n");
	printf("Size: %zd\n", size);

	printf("Elements: [");
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		if (item == NULL)
			PyErr_Print();

		repr = PyObject_Repr(item);
		elementStr  = PyUnicode_AsUTF8(repr);

		if (i < size - 1)
			printf(", ");

		Py_XDECREF(repr);
	}
	printf("]\n");
}
