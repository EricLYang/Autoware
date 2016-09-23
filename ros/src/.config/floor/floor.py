#!/usr/bin/env python

import sys
import os
import Image

if __name__ == "__main__":
	argv = sys.argv[1:]
	if len(argv) < 2:
		print('usage: {} <img_path> <meger/img_width> [ org_x,org_y,org_z ]'.format(sys.argv[0]))
		sys.exit(0)

	odir = os.path.dirname(__file__)
	img_path = argv[0]
	m_w = float( argv[1] )
	org = [ float(e) for e in argv[2].split(',') ] if len(argv) > 2 else [ 0, 0, 0 ]

	img = Image.open(img_path)
	(w, h) = img.size
	m_h = m_w * h / w

	s = ''
	fn = os.path.join(odir, 'floor-template.dae')
	with open(fn, 'r') as f:
		s = f.read()

	fn = os.path.relpath(img_path, odir)
	s = s.format(fn, org[0], org[1], org[2], m_w, m_h)

	fn = os.path.join(odir, 'floor.dae')
	with open(fn, 'w') as f:
		f.write(s)

	sys.exit(0)
# EOF
