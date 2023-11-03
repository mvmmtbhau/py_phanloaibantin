import pickle
import numpy as np
import os
import regex as re

from sklearn.naive_bayes import MultinomialNB
from flask import request
from .tien_xu_ly_van_ban import convert_unicode,chuan_hoa_dau_cau_tieng_viet,word_tokenize, remove_stopwords

def tien_xu_ly_van_ban(document):
    # chuẩn hóa unicode
    document = convert_unicode(document)
    # chuẩn hóa cách gõ dấu tiếng Việt
    document = chuan_hoa_dau_cau_tieng_viet(document)
    # tách từ
    document = word_tokenize(document, format="text")
    # đưa về lower
    document = document.lower()
    # xóa các ký tự không cần thiết
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',document)
    # xóa khoảng trắng thừa
    document = re.sub(r'\s+', ' ', document).strip()

    document = remove_stopwords(document)
    return document

model = pickle.load(open(os.path.join("D:\Learn_space\KhaiKhoang\model","logistic.pkl"), 'rb'))

def phan_loai_ban_tin():
    data = request.form['bantin']

    document = tien_xu_ly_van_ban(data)
    y_pred = model.predict([document])
    
    if y_pred == 0:
        return "Du lịch"
    elif y_pred == 1:
        return "Thể thao"
    elif y_pred == 2:
        return "Đời sống"