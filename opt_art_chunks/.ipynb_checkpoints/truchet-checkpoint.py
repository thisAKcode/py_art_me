{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Truchet:\n",
    "    \"\"\"Base class for a Truchet tiling.\"\"\"\n",
    "\n",
    "    def __init__(self, width, height, s):\n",
    "        \"\"\"Initialize the class with image size and tile size, s.\"\"\"\n",
    "\n",
    "        self.width, self.height = width, height\n",
    "        self.s = s\n",
    "        self.nx, self.ny = int(width // s), int(height // s)\n",
    "        self.fo = None\n",
    "\n",
    "    def preamble(self):\n",
    "        \"\"\"The usual SVG preamble, including the image size.\"\"\"\n",
    "\n",
    "        print('<?xml version=\"1.0\" encoding=\"utf-8\"?>\\n'\n",
    "\n",
    "        '<svg xmlns=\"http://www.w3.org/2000/svg\"\\n' + ' '*5 +\n",
    "           'xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"{}\" height=\"{}\" >'\n",
    "                .format(self.width, self.height), file=self.fo)\n",
    "\n",
    "    def defs_decorator(func):\n",
    "        \"\"\"For convenience, wrap the CSS styles with the needed SVG tags.\"\"\"\n",
    "\n",
    "        def wrapper(self):\n",
    "            print(\"\"\"\n",
    "            <defs>\n",
    "            <style type=\"text/css\"><![CDATA[\"\"\", file=self.fo)\n",
    "\n",
    "            func(self)\n",
    "\n",
    "            print(\"\"\"]]></style>\n",
    "            </defs>\"\"\", file=self.fo)\n",
    "        return wrapper\n",
    "\n",
    "    def svg_shape(self, *args, **kwargs):\n",
    "        \"\"\"Override this function in the derived class.\"\"\"\n",
    "\n",
    "    def make_svg(self, filename, *args, **kwargs):\n",
    "        \"\"\"Create the tiling image as an SVG file with name filename.\n",
    "\n",
    "        Custom arguments are passed to the derived class's svg_shape method.\n",
    "\n",
    "        \"\"\"\n",
    "\n",
    "        self.fo = open(filename, 'w')\n",
    "        self.preamble()\n",
    "        self.svg_styles()\n",
    "        self.svg_shape(*args, **kwargs)\n",
    "        print('</svg>', file=self.fo)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
