{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f957bce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "12\n",
      "123\n",
      "1234\n"
     ]
    }
   ],
   "source": [
    "row=4\n",
    "for row in range(1,row+1):\n",
    "    for column in range(1,row+1):\n",
    "        print(column,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "43bae1a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "12\n",
      "123\n",
      "1234\n",
      "12345\n"
     ]
    }
   ],
   "source": [
    "row=5\n",
    "for row in range(1,row+1):\n",
    "    for column in range(1,row+1):\n",
    "        print(column,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7a74d02e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "12\n",
      "123\n",
      "1234\n",
      "12345\n",
      "123456\n",
      "1234567\n",
      "12345678\n",
      "123456789\n",
      "12345678910\n"
     ]
    }
   ],
   "source": [
    "row=10\n",
    "for row in range(1,row+1):\n",
    "    for column in range(1,row+1):\n",
    "        print(column,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "29e58147",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "12\n",
      "123\n",
      "1234\n",
      "12345\n",
      "123456\n",
      "1234567\n",
      "12345678\n",
      "123456789\n",
      "12345678910\n",
      "1234567891011\n",
      "123456789101112\n",
      "12345678910111213\n",
      "1234567891011121314\n",
      "123456789101112131415\n",
      "12345678910111213141516\n",
      "1234567891011121314151617\n",
      "123456789101112131415161718\n",
      "12345678910111213141516171819\n",
      "1234567891011121314151617181920\n",
      "123456789101112131415161718192021\n",
      "12345678910111213141516171819202122\n",
      "1234567891011121314151617181920212223\n",
      "123456789101112131415161718192021222324\n",
      "12345678910111213141516171819202122232425\n",
      "1234567891011121314151617181920212223242526\n",
      "123456789101112131415161718192021222324252627\n",
      "12345678910111213141516171819202122232425262728\n",
      "1234567891011121314151617181920212223242526272829\n",
      "123456789101112131415161718192021222324252627282930\n",
      "12345678910111213141516171819202122232425262728293031\n",
      "1234567891011121314151617181920212223242526272829303132\n",
      "123456789101112131415161718192021222324252627282930313233\n",
      "12345678910111213141516171819202122232425262728293031323334\n",
      "1234567891011121314151617181920212223242526272829303132333435\n",
      "123456789101112131415161718192021222324252627282930313233343536\n",
      "12345678910111213141516171819202122232425262728293031323334353637\n",
      "1234567891011121314151617181920212223242526272829303132333435363738\n",
      "123456789101112131415161718192021222324252627282930313233343536373839\n",
      "12345678910111213141516171819202122232425262728293031323334353637383940\n",
      "1234567891011121314151617181920212223242526272829303132333435363738394041\n",
      "123456789101112131415161718192021222324252627282930313233343536373839404142\n",
      "12345678910111213141516171819202122232425262728293031323334353637383940414243\n",
      "1234567891011121314151617181920212223242526272829303132333435363738394041424344\n",
      "123456789101112131415161718192021222324252627282930313233343536373839404142434445\n"
     ]
    }
   ],
   "source": [
    "row=45\n",
    "for row in range(1,row+1):\n",
    "    for column in range(1,row+1):\n",
    "        print(column,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "62ee90ad",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12345\n",
      "1234\n",
      "123\n",
      "12\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(a,0,-1):\n",
    "    for b in range(1,a+1):\n",
    "        print(b,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2014ca68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55555\n",
      "4444\n",
      "333\n",
      "22\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(a,0,-1):\n",
    "    for b in range(1,a+1):\n",
    "        print(a,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d755e9e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****\n",
      "****\n",
      "***\n",
      "**\n",
      "*\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(a,0,-1):\n",
    "    for b in range(1,a+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "11e8a8ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "row=5\n",
    "for row in range(1,row+1):\n",
    "    for column in range(1,row+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "87af2129",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****\n",
      "***\n",
      "*\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(a,0,-2):\n",
    "    for b in range(1,a+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "9328829a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "***\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(1,a+1,2):\n",
    "    for b in range(1,a+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "5ff205f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12345\n",
      "123\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "for a in range(a,0,-2):\n",
    "    for b in range(1,a+1):\n",
    "        print(b,end=\"\")\n",
    "    print(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be23bfad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
