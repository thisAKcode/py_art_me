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
    "class TruchetArcs(Truchet):\n",
    "    \"\"\"A class for creating a Truchet tiling of arcs.\"\"\"\n",
    "\n",
    "    def __init__(self, width, height, s, colour):\n",
    "        super(TruchetArcs, self).__init__(width, height, s)\n",
    "        self.colour = colour\n",
    "\n",
    "    @Truchet.defs_decorator\n",
    "    def svg_styles(self):\n",
    "        print('.arc {{ stroke: {}; stroke-width: 3px; fill: none; }}'\n",
    "              .format(self.colour), file=self.fo)\n",
    "\n",
    "\n",
    "    def svg_shape(self, r=None, rule=None):\n",
    "        \"\"\"A Truchet figure based on interlinking circular arcs.\"\"\"\n",
    "\n",
    "        def arc_path(A, B, r):\n",
    "            \"\"\"Semicircular arc path from A=(x0,y0) to B=(x1,y1), radius r.\"\"\"\n",
    "\n",
    "            print('<path d=\"M{},{} A{},{} 0 0 1 {} {}\" class=\"arc\"/>'.format(\n",
    "                  *A, r, r, *B), file=self.fo)\n",
    "\n",
    "        if rule is None:\n",
    "            rule = lambda ix, iy: random.randint(0,1)\n",
    "\n",
    "        if not r:\n",
    "            r = self.s / 2\n",
    "        for ix in range(self.nx):\n",
    "            for iy in range(self.ny):\n",
    "                p = rule(ix, iy)\n",
    "                x0, y0 = ix*self.s, iy*self.s\n",
    "                A, B = (x0,y0 + r), (x0 + r,y0 + self.s),\n",
    "                C, D = (x0 + self.s,y0 + r), (x0 + r,y0)\n",
    "                if p:\n",
    "                    arc_path(A, B, r)\n",
    "                    arc_path(C, D, r)\n",
    "                else:\n",
    "                    arc_path(D, A, r)\n",
    "                    arc_path(B, C, r)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    truchet = TruchetArcs(600, 400, 20, colour='#2e88cf')\n",
    "    truchet.make_svg('arcs.svg')"
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
