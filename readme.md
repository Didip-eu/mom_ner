Named Entity Recognition in Monasterium.net abstracts
=====================================================

Experiments during internship@acdh-dh, summer 2021
supervised by Matthias Schlögl, Georg Vogeler

# Annotation Guidelines:
- The data set uses only LOC, PERS, and ORG.
- We do not use nested annotations: e.g. `ORG[Kloster St. Peter]` and not `ORG[Kloster LOC[St. Peter]]`.
- The annotated string should contain all information necessary to identify the type: e.g. `PERS[Eb von Salzburg]`.
- We don't use `GPE`, as political entities are not a medieval concept. `Hallein, Mühldorf, Böhmen, Österreich, Steiermark` etc. are `LOC`.
- Lists of organisation use `ORG` even if in the list the identifier for being an organisation can only be annotated in the first or last list entry: `die ORG[Pfarrkirchen zu Mühldorf], ORG[Laufen] und ORG[Pettau]" oder "ORG[Salzburger] und ORG[Seckauer Diözese]`.
- names quoted from the original are annotated separately from the modernized name: `PERS[Laurenz Schmid] (PERS[Loritzen dem smit]) zu LOC[Gaisbach] (LOC[Gaispach])`.

