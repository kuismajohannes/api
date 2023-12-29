Tarvittavat ohjeet API:n toimimiseen:

Luo Virtual Environment. Ctrl + Shift + P -> Python. Create Environment... -> Venv -> Python 3.11.1 64-bit. Katso että venv asennetaan sille tarkoitettuun omaan kansioon.
Asenna Uvicorn. Kirjoita terminaaliin: pip install uvicorn.
Asenna FASTAPI. Kirjoita terminaaliin: pip install fastapi.
Aktivoi venv kirjoittamalla terminaaliin .\.venv\Scripts\activate
Venvin aktivoiduttua kirjoita terminaaliin uvicorn main:app --reload
Terminaaliin pitäisi tulla linkki sivustolle http://127.0.0.1:8000.
Mene http://127.0.0.1:8000/docs näkeäksesi APIN toiminnot.

Kun teet uuden pelaajan, lisää pelaajan nimi manuaalisesti Request Bodyssa hipsuihin. 
Kun haluat lisätä pelaajalle eventin, lisää eventin type ja detail manuaalisesti Request bodyssa hipsuihin. 