#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_bytes - function that prints info about a python bytes
 * @p: is a python Object
 */
void print_python_bytes(PyObject *p)
{
	long int i;
	long int size;
	char *word;

	size = (((PyVarObject *)(p))->ob_size);
	word = ((PyBytesObject *)p)->ob_sval;
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", word);
		if (size < 10)
		{
			printf("  first %ld", size + 1);
		}
		else
		{
			size = 9;
			printf("  first 10");
		}
		printf(" bytes:");
		for (i = 0; i <= size; i++)
		{
			if (word[i] < 0)
				printf(" %02x", (256 + word[i]));
			else
				printf(" %02x", word[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	fflush(stdout);
}
/**
 * print_python_float - function that prints
 *info about float elements in python
 * @p : is a python object
 */
void print_python_float(PyObject *p)
{
	double vari = (((PyFloatObject *)(p))->ob_fval);
	char *res = NULL;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		res = PyOS_double_to_string(vari, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
		printf("  value: %s\n", res);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	fflush(stdout);
}
/**
 * print_python_list - function that prints info about lists in python
 * @p : is a python object
 */
void print_python_list(PyObject *p)
{
	unsigned int i, j = (((PyVarObject *)(p))->ob_size);
	PyObject *item;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = ");
		printf("%ld\n", (((PyVarObject *)(p))->ob_size));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < j; i++)
		{
			item = ((PyListObject *)p)->ob_item[i];
			printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
			if (PyFloat_Check(item))
			{
				print_python_float(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
	fflush(stdout);
}
