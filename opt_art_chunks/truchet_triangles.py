{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "from truchet import Truchet\n",
    "\n",
    "class TruchetTriangles(Truchet):\n",
    "    \"\"\"A class for creating a Truchet tiling of triangles.\"\"\"\n",
    "\n",
    "    def __init__(self, width, height, s, colour):\n",
    "        super(TruchetTriangles, self).__init__(width, height, s)\n",
    "        self.colour = colour\n",
    "\n",
    "    @Truchet.defs_decorator\n",
    "    def svg_styles(self):\n",
    "        print('.tri {{ stroke: none; fill: {}; }}'.format(self.colour),\n",
    "              file=self.fo)\n",
    "\n",
    "\n",
    "    def svg_shape(self, rule=None):\n",
    "        \"\"\"A Truchet figure based on triangles.\n",
    "\n",
    "        The four triangle orientations to choose from in each square are:\n",
    "                                xx x. xx .x\n",
    "                                .x xx x. xx\n",
    "\n",
    "        \"\"\"\n",
    "\n",
    "        if rule is None:\n",
    "            rule = lambda ix, iy: random.randint(0,4)\n",
    "\n",
    "        def triangle_path(A, B, C):\n",
    "            \"\"\"Output a triangular path with vertices at A, B, C.\"\"\"\n",
    "\n",
    "            print('<path d=\"M{},{} L{},{} L{},{}z\" class=\"tri\"/>'.format(\n",
    "                    *A, *B, *C), file=self.fo)\n",
    "\n",
    "        for ix in range(self.nx):\n",
    "            for iy in range(self.ny):\n",
    "                x0, y0 = ix*self.s, iy*self.s\n",
    "                x1, y1 = (ix+1)*self.s, (iy+1)*self.s\n",
    "                p = rule(ix, iy)\n",
    "                if p == 0:\n",
    "                    triangle_path((x0, y0), (x1, y0), (x1, y1))\n",
    "                elif p == 1:\n",
    "                    triangle_path((x0, y0), (x0, y1), (x1, y1))\n",
    "                elif p == 2:\n",
    "                    triangle_path((x0, y0), (x1, y0), (x0, y1))\n",
    "                else:\n",
    "                    triangle_path((x1, y0), (x1, y1), (x0, y1))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    truchet = TruchetTriangles(600, 400, 20, colour='#882ecf')\n",
    "    truchet.make_svg('triangles.svg')"
   ]
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
