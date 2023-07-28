# USERGUIDE
### Model Word Embedding

1. menggunakan dataset dump wikipedia latest https://dumps.wikimedia.org/idwiki/latest/
2. Run code ```Create Embedding.ipynb```
3. Hasil ```wiki_id.txt``` dilakukan training menggunakan word2vec program ```train_emb.py```, default word2vec adalah CBOW
4. Hasil training berupa ```id_word2vec_300_new.txt``` akan digunakan pada tahap training model

### Model Chatbot
#### Tanpa Cross Validation
1. Run file ```code.ipynb```
2. Import library
3. Load dataset ```faq2.csv```
4. Lakukan preprocessing mulai remove punctuation, case folding, ubah kata tidak baku menjadi kata baku, menghapus stopwords, stemming, tokenisasi. 
5. Load hasil training word embedding ```id_word2vec_300_new.txt``` dan tentukan weight embedding
6. Tentukan layer model 
7. Train menggunakan fungsi ```model.fit()``` 
8. Didapatkan model dengan format .hdf5
9. Evaluasi matriks precision, recall, dan f1-score 

#### Cross Validation
*Step 2-5 sama dengan tanpa cross-val*
1. Run file ```code_cv.ipynb```
2. Tentukan jumlah k fold (pada case ini k=5)
3. Iterasi sebanyak jumlah fold dan diperoleh model tiap iterasi dengan format .hdf5

### Implementasi website
*Pada tahapa pelatihan didapatkan 3 file pickle yaitu tag.pickle, slangs.pickle, dan tokenizer.pickle*
1. Buka program ```app.py``` pada link berikut 
2. Load model .hdf5
3. Load semua file pickle
4. Run app.py melalui command prompt dengan command ```python app.py```
5. Run XAMPP untuk akses database mySQL
6. Akses ```http://127.0.0.1:5000/``` melalui web browser