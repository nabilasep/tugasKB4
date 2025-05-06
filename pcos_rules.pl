% Fakta dan aturan deteksi PCOS
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

pcos(X) :- gejala_pos(irregular_cycle), gejala_pos(high_testosterone), gejala_pos(ovarian_cysts).

% Gejala-gejala yang ditanyakan
gejala(irregular_cycle, "Apakah Anda mengalami siklus menstruasi tidak teratur?").
gejala(high_testosterone, "Apakah Anda memiliki tanda-tanda hormon testosteron tinggi, seperti pertumbuhan rambut berlebih?").
gejala(ovarian_cysts, "Apakah hasil pemeriksaan menunjukkan adanya kista pada ovarium?").

% Menyimpan jawaban
tambah_gejala(X) :- assertz(gejala_pos(X)).
hapus_gejala(X) :- assertz(gejala_neg(X)).