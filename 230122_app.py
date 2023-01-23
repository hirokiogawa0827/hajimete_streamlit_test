import streamlit as st
from PIL import Image
import pandas as pd

st.title('ヒロキアプリ')

st.subheader('はじめてのDeploy')
st.text('使いやすくて楽しい♪Webアプリを作るぞ！！')
st.caption('This is testapp')
code = '''
import streamlit as st
st.title('ヒロキアプリ')
'''
st.code(code, language='python')

# ボタン
with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    age_category =st.radio(
        '年齢層',('子ども（１８歳未満）', '大人（１８歳以上）')
    )
    hobby = st.multiselect(
        '趣味', ('読書','プログラミング','アニメ/映画','釣り','料理')
    )
    
    import datetime

    d = st.date_input(
        "When\'s your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)


    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)
    
    color = st.select_slider(
        'Select a color of the rainbow',
        options=['red','orange','yellow','green','blue','indigo','violet']
    )
    st.write('My favorite color is', color)
    
    submit_btn = st.form_submit_button('Submit')
    cancel_btn = st.form_submit_button('Cancel')
    print(f'submit_btn: {submit_btn}')
    print(f'cancel_btn: {cancel_btn}')
    
    if submit_btn:
        st.text(f'ようこそ！{name}さん!{address}に住んでますね！')
        st.text(f'年齢層:{age_category}')
        st.text(f'趣味: {", ".join(hobby)}が好き！')
        st.text(f'虹の色: {color}')

# file = 'PL.xlsx'
# df = pd.read_excel(file)
# df = df.fillna('')
# st.dataframe(df)

# 画像
col1,col2 = st.columns(2)
with col1:
    st.header("更くん")
    image = Image.open('Sara_weight.jpg')
    st.image(image, width=200)
    st.write('1才１ヶ月になりました！')
with col2:
    st.header("食事")
    image = Image.open('.\data\Shokuji3.jpg')
    st.image(image, width=200)
    st.write('いつも豊富なごちそうです！感謝です！ハレルヤ！')
    
col3,col4 = st.columns(2)    
with col3:
    image = Image.open('.\data\Shokuji1.jpg')
    st.image(image, width=200)
    
with col4:
    image = Image.open('.\data\Shokuji2.jpg')
    st.image(image, width=200)

# 動画
# st.video("https://www.youtube.com/watch?v=4nsTce1Oce8&t=1314s")


