Named Entity Recognition in Monasterium.net abstracts
=====================================================

Experiments during internship@acdh-dh, summer 2021
supervised by Matthias Schlögl, Georg Vogeler
annotations by Varvara Arzt and Nadine Sutor

# Annotation Guidelines:
1. The data set uses only LOC, PERS, and ORG.
1. We do not use nested annotations: e.g. `ORG[Kloster St. Peter]` and not `ORG[Kloster LOC[St. Peter]]`.
1. The annotated string should contain all information necessary to identify the type: e.g. `PERS[Eb von Salzburg]`.
1. We don't use `GPE`, as political entities are not a medieval concept. `Hallein, Mühldorf, Böhmen, Österreich, Steiermark` etc. are `LOC`.
1. Lists of organisation use `ORG` even if in the list the identifier for being an organisation can only be annotated in the first or last list entry: `die ORG[Pfarrkirchen zu Mühldorf], ORG[Laufen] und ORG[Pettau]" oder "ORG[Salzburger] und ORG[Seckauer Diözese]`.
1. Acting persons referenced only their role ("Der Kaiser schenkt ...") are not annotated.
1. names quoted from the original are annotated separately from the modernized name: `PERS[Laurenz Schmid] (PERS[Loritzen dem smit]) zu LOC[Gaisbach] (LOC[Gaispach])`.
1. Agents (e.g. acting as issuers or recepients of a legal act) like monasteries, churches, chapels and similar are usually ORG: e.g. `XY schenkt dem PERS[Abt Ulrich] und dem ORG[Convent von Melk]". Only if the very building of the church is concerned (e.g. for construction) they are to be annotated as LOC.
1. `Pflege X`, `Pfleggericht Y` usually indicate a LOC, if they are not referenced as agents (`Das Urteil des Pfleggerichts Y` => ORG). The same is valid for `Festung`, `Schloss` and similar: prefer `LOC` if it is not an agent.
1. Similar approach for synods, councils etc.: if the council acts (e.g. making decisions) it is an ORG, while references to the "Event" are LOC: `auf dem Konzil zu LOC[Basel]`). I in doubt, use LOC.
1. offices are usually part of the actor: `PERS[Vizedom von Leibnitz]`, `ORG[Forstamt zu Spielfeld]`, `PERS[Pfarrer von St. Michael]` , `ORG[Pfarrkirche von St. Peter]`.
1. Distinguishing LOC and ORG is hard. In doubt, prefer LOC.
1. Types of locations are usually not an individual namem so the standard annotation is: `ein Gut zu LOC[Haselbach]`, `der Hof LOC[Ainöd bei Kaprun]` or `ein Gut unterm LOC[Rain].
1. Places and persons named in the bibliography are not annotated.
1. Places being part of currency names (e.g. "50 Pfd. Rgsbrgr. Pfge" for "50 Pfund Regensburger Pfennige", "Sbger." for "Salzburger Groschen", "rhein." for "rheinische Gulden" etc. are not annotated.
1. `Markus Jude von Wien` or `Johannes Bürger von Hallein` are annotated as PERS, including the role name and the place name.
1. The `+` in front of a person name usually denotes "late" / "verstorben" and can be included in the PERS annotation `die Vormünder der PERS[Margarethe], Tochter des PERS[+ Virgil Rauhenberger]`

... tbc ...

# Hints on abbreviations:
- `Pfgf` = Pfalzgraf
- `Reg.` (in bibliography) = Regesten
- `K.` = Kaiser or König
- `P.` = Papst
- `Erw.` = Erwählt

