Named Entity Recognition in Monasterium.net abstracts
=====================================================

Experiments during internship@acdh-dh, summer 2021
supervised by Matthias Schlögl, Georg Vogeler
annotations by Varvara Arzt and Nadine Sutor

# Annotation Guidelines:
- The data set uses only LOC, PERS, and ORG.
- We do not use nested annotations: e.g. `ORG[Kloster St. Peter]` and not `ORG[Kloster LOC[St. Peter]]`.
- The annotated string should contain all information necessary to identify the type: e.g. `PERS[Eb von Salzburg]`.
- We don't use `GPE`, as political entities are not a medieval concept. `Hallein, Mühldorf, Böhmen, Österreich, Steiermark` etc. are `LOC`.
- Lists of organisation use `ORG` even if in the list the identifier for being an organisation can only be annotated in the first or last list entry: `die ORG[Pfarrkirchen zu Mühldorf], ORG[Laufen] und ORG[Pettau]" oder "ORG[Salzburger] und ORG[Seckauer Diözese]`.
- Acting persons referenced only their role ("Der Kaiser schenkt ...") are not annotated.
- names quoted from the original are annotated separately from the modernized name: `PERS[Laurenz Schmid] (PERS[Loritzen dem smit]) zu LOC[Gaisbach] (LOC[Gaispach])`.
- Agents like monasteries, churches, chapels and similar are usually ORG. Only if the very building of the church is concerned (e.g. for construction) they are to be annotated as LOC.
- `Pflege X`, `Pfleggericht Y` usually indicate a LOC, if they are not referenced as agents (`Das Urteil des Pfleggerichts Y` => ORG). The same is valid for `Festung`, `Schloss` and similar: prefer `LOC` if it is not an agent.
- Similar approach for synods, councils etc.: if the council acts (e.g. making decisions) it is an ORG, while references to the "Event" are LOC: `auf dem Konzil zu LOC[Basel]`). I in doubt, use LOC.
- offices are usually part of the actor: `PERS[Vizedom von Leibnitz]`, `ORG[Forstamt zu Spielfeld]`, `PERS[Pfarrer von St. Michael]` , `ORG[Pfarrkirche von St. Peter]`.
- Distinguishing LOC and ORG is hard. In doubt, prefer LOC.
- Types of locations are usually not an individual namem so the standard annotation is: `ein Gut zu LOC[Haselbach]`, `der Hof LOC[Ainöd bei Kaprun]` or `ein Gut unterm LOC[Rain].
- Places and persons named in the bibliography are not annotated.
- Places being part of currency names (e.g. "50 Pfd. Rgsbrgr. Pfge" for "50 Pfund Regensburger Pfennige", "Sbger." for "Salzburger Groschen", "rhein." for "rheinische Gulden" etc. are not annotated.
- `Markus Jude von Wien` or `Johannes Bürger von Hallein` are annotated as PERS, including the role name and the place name.
- The `+` in front of a person name usually denotes "late" / "verstorben" and can be included in the PERS annotation `die Vormünder der PERS[Margarethe], Tochter des PERS[+ Virgil Rauhenberger]`

... tbc ...

# Hints on abbreviations:
- `Pfgf` = Pfalzgraf
- `Reg.` (in bibliography) = Regesten
- `K.` = Kaiser or König
- `P.` = Papst
- `Erw.` = Erwählt

