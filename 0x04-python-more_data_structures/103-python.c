#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - prints info about python list
 * @p: points to a PyObject list
 * Return: returns nothing
 */
void print_python_list(PyObjec *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*]Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, PyTYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - Print info about python bytes object
 * @p: Pointer to a PyObject
 * Return: returns nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str_bytes;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_size(p);
	str_bytes = ((PyBytesObject *)p)->ob_sval;
	printf("[.] bytes object info\n");
	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", str_bytes);
	if (size > 10)
		size = 10;
	printf(" first %zd bytes: ", size);
	for (i = 0; i < size; ++i)
	{
		printf("%02x", (unsigned char)bytes_str[i]);
		if (i < size - 1)
		printf(" ");
	}
	printf("\n");
}

