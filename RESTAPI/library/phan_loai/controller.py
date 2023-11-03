from flask import Blueprint, render_template, request, redirect, url_for

from .service import phan_loai_ban_tin

routes = Blueprint("phan_loai", __name__)

@routes.route('/home')
def home():
    data=''
    if request.args.get('data'):
        data = request.args.get('data')
    return render_template("index.html", label="Bản tin sau khi phân loại: "+data)


@routes.route('/phan-loai/nhanh', methods = ['POST'])
def phan_loai1():   
    label = phan_loai_ban_tin()
    return redirect(url_for('.home', data = label))

