all: GL-Antique.ttf GL-AntiquePlus.ttf

GL-Antique.ttf: GL-Antique.sfd ff_generate.py
	fontforge -lang=py -script $(word 2, $^) $< $@

GL-Antique.otf: GL-Antique.sfd ff_generate.py
	fontforge -lang=py -script $(word 2, $^) $< $@

GL-AntiquePlus.ttf: GL-AntiquePlus.sfd ff_generate.py
	fontforge -lang=py -script $(word 2, $^) $< $@

GL-AntiquePlus.otf: GL-AntiquePlus.sfd ff_generate.py
	fontforge -lang=py -script $(word 2, $^) $< $@

