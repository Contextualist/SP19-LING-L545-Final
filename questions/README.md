The merged question set is prepared by

```
diff -U 9999999 chv_ipa/questions_dnn.hed eng/questions_dnn.hed > ehv/questions_dnn.hed 
vim ehv/questions_dnn.hed # trim diff marks
cp chv_ipa/questions_dnn.hed.key ehv/questions_dnn.hed.key
diff -U 9999999 chv_ipa/questions_dnn.hed.cont eng/questions_dnn.hed.cont > ehv/questions_dnn.hed.cont
vim ehv/questions_dnn.hed.cont # trim diff marks
python merge_val.py chv_ipa/questions_dnn.hed.values eng/questions_dnn.hed.values > ehv/questions_dnn.hed.values
```

Note that question\_dur.hed.\* have the exact same content as questions\_dnn.hed.\*
