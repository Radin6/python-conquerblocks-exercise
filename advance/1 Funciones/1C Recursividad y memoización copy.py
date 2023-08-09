{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ejercicio 1 - Factorial\n",
    "\n",
    "funcion recursiva llama factorial que calcule el factorial de un num entero positivo\n",
    "el producto de todos lo num enteros positivos desde 1 hasta n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mCannot execute code, session has been disposed. Please try restarting the Kernel."
     ]
    },
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mThe Kernel crashed while executing code in the the current cell or a previous cell. Please review the code in the cell(s) to identify a possible cause of the failure. Click <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "fact = 1\n",
    "n = 0\n",
    "\n",
    "def factorial(n):\n",
    "    if n == 1 or n == 0:\n",
    "        return 1\n",
    "    else:\n",
    "        factorial(n-1)*factorial(n)\n",
    "\n",
    "factorial(int(input(\"Ingrese el número para calcular el factorial\")))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
