import streamlit as st
import streamlit.components.v1 as components
import lorem
import pandas as pd
from PIL import Image
import plotly.graph_objects as go
import plotly_express as px
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')
CURRENT_THEME = 'Custom Theme'

# ws
df = pd.read_csv("google_trends.csv")
df['Week'] = pd.to_datetime(df['Week'])
df_media = pd.read_csv('social_media.csv')
df_marketing = pd.read_csv('marketing_data.csv')
df_animation = pd.read_csv('social_media_animation.csv')

# Sentiment Analysis Instagram
df_sainstagram = pd.read_csv('sa_instagram.csv')
pie_sainstagram = df_sainstagram.Sentiment.value_counts()
df2 = pd.DataFrame(pie_sainstagram)
pie_sainstagram = pie_sainstagram.reset_index()
pie_sainstagram.columns = ['sentiment','value']

# Sentiment Analysis YouTube
df_youtube = pd.read_csv('sa_youtube.csv')
df3 = df_youtube.Sentiment.value_counts()
pie_sayoutube = pd.DataFrame(df3)
pie_sayoutube = pie_sayoutube.reset_index()
pie_sayoutube.columns = ['sentiment','value']

# Sentiment Analysis TikTok
df_tiktok = pd.read_csv('sa_tiktok.csv')
pie_tiktok = df_tiktok.Sentiment.value_counts()
pie_satiktok = pie_tiktok.reset_index()
pie_satiktok.columns = ['sentiment','value']

# Sentiment Analysis Facebook
df_facebook = pd.read_csv('sa_facebook.csv')
pie_facebook = df_facebook.Sentiment.value_counts()
pie_safacebook = pie_facebook.reset_index()
pie_safacebook.columns = ['sentiment','value']

# Demographic Instagram
de_instagram = pd.read_csv('demo_instagram.csv')

# Demographic YouTube
de_youtube = pd.read_csv('demo_youtube.csv')

# Demographic TikTok
de_tiktok = pd.read_csv('demo_tiktok.csv')

# Demographic Facebook
de_facebook = pd.read_csv('demo_facebook.csv')

# Demographic all
de_all = pd.read_csv('demografi_all.csv')

# Influencer Marketing Stats
df_influencer = pd.read_csv('influencer.csv')

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# Navigation Bar
page = option_menu(
    menu_title = None,
    options = ['Project','Documentation','Contact'],
    icons = ['house','book','envelope'],
    default_index=0,
    orientation='horizontal'
)

if page == 'Project':

    if 'demography' not in st.session_state:
        st.session_state.demography = '...'
    if 'content' not in st.session_state:
        st.session_state.content = '...'

    st.markdown("---")

    st.title("Social Media Marketing: Sebuah Perspektif Data untuk Indonesia")
    st.subheader(""""Be where the world is going." -Beth Comstock""")

    # Problem Definition
    st.markdown('''<p class="big-font">Sebanyak 
            191 juta warga Indonesia, 70% dari keseluruhan masyarakat, merupakan pengguna aktif media sosial pada Januari 2022 (DataReportal). 
            Melihat data tersebut, bukan hanya perusahaan besar, bahkan warga biasa
            dapat menyusun strategi memaksimalkan opportunity untuk menjangkau pelanggan sebanyak-banyaknya
            melalui media sosial. Lalu timbul pertanyaan, media sosial apa yang memiliki potensi mencapai market terbesar?
            Bisakah data menjawabnya?</p>''', unsafe_allow_html=True)
    top1, top2 = st.columns([1,1])
    with top1:
        fig2 = px.bar(
                      df_animation,
                      y='media',
                      x='value',
                      color='media',
                      animation_frame='year',
                      animation_group='media',
                      height= 450,
                      range_x=[0,3000],
                      orientation='h')
        fig2.update_layout( xaxis_title="Pengguna Aktif Bulanan (jutaan)", yaxis_title="Media Sosial",showlegend = False)
        st.plotly_chart(fig2, use_container_width=True)
        st.caption('Pengguna Aktif Media Sosial Terbanyak dalam jutaan (hootsuite.com)')
    with top2:
        st.markdown('---')
        st.markdown('''<p class="big-font"> Nama-nama media sosial di samping tidaklah asing bagi masyarakat Indonesia, apalagi
                setelah dilanda situasi pandemi, media sosial tersebut sudah bersinonim dengan aktivitas kita sehari-hari.
                Namun, media sosial yang berada di chart ini memiliki bidang spesialisasi yang berbeda-beda, sehingga tidak semua
                mampu untuk dijadikan platform marketing yang dapat diandalkan. Platform marketing yang diperlukan adalah situs dengan 
                fitur iklan yang dapat memenuhi kebutuhan marketing sang pengusaha. Oleh karena itu, dibutuhkan opini dari pihak yang kredibel
                untuk memberikan gambaran media sosial yang tepat untuk dijadikan platform marketing.</p>''', unsafe_allow_html=True)


    bot1, bot2 = st.columns([2,1])
    with bot1:
        st.markdown('---')
        st.markdown('''<p class="big-font">Sebanyak 93% dari agensi marketing profesional di Amerika Serikat akan menggunakan 
                sosial media sebagai platform marketing.
                Sepuluh media sosial dengan hasil survey terbaik tersebut bukanlah acak, melainkan mereka adalah media sosial yang 
                memiliki fitur dan potensi untuk marketing yang jauh lebih besar dibandingkan dengan platform yang lainnya.
                Hal tersebut memberikan implikasi lebih bahwa para marketer profesional menggunakan banyak pertimbangan
                dalam pemilihan platform yang tepat. Untuk membuktikan implikasi tersebut, dapat dilakukan korelasi antara
                kedua data yang telah ditunjukkan.
                </p>''', unsafe_allow_html=True)
    with bot2:
        st.markdown('---')
        data_m = px.bar(df_marketing,
                    y='value',
                    x='media',
                    color = 'media',
                    color_discrete_map={'Instagram': '#AB63FA','TikTok': '#19D3F3','YouTube':'rgb(228,26,28)','Facebook':'#636EFA'},
                    height= 300,
                    range_y=[0,100],
                    orientation='v')
        data_m.update_layout(xaxis_title="Media Sosial", yaxis_title="Persentase Marketer Memilih (%)",showlegend = False)
        layout_m = data_m['layout'].update(margin=dict(l=0,r=0,b=0,t=0),height=300)

        fig_m = dict(data=data_m, layout=layout_m)
        st.plotly_chart(fig_m, use_container_width=True)
        st.caption("Pilihan Media Sosial untuk Marketing dalam persen (statista.com)")

    # Analisis korelasi marketer dan jumlah user
    act1,act2 = st.columns([1,1])
    with act1:
        summary = pd.read_csv('summary.csv')
        fig_sum = px.scatter(summary, x="market", y="users",color='media',color_discrete_map={'Instagram': '#AB63FA','TikTok': '#19D3F3','YouTube':'red','Facebook':'#636EFA'},size = 'age', trendline='ols',trendline_scope = 'overall',trendline_color_override = 'blue')
        fig_sum.update_layout( xaxis_title="Persentase Marketer Memilih (%)", yaxis_title="Pengguna Aktif Bulanan (jutaan)")
        st.plotly_chart(fig_sum, use_container_width=True)
        st.caption('Analisis Korelasi antara Jumlah User dan Trend Marketing')
    with act2:
        st.markdown('---')
        st.markdown('''<p class="big-font">
                Dengan menggambarkan korelasi dari kedua data di atas, didapatkan hubungan antara popularitas sebuah media sosial dengan
                marketability menurut para profesional yaitu berkorelasi positif tetapi lemah, sehingga dapat disimpulkan bahwa
                masih terdapat variabel lain yang lebih berkorelasi dengan marketability.
                Dari seluruh media sosial di kedua data, hanya 7 media sosial yang konsisten berada di keduanya.
                Hal ini dapat disebabkan karena platform seperti Whatsapp dan WeChat memiliki fitur periklanan yang terbatas.
                Terdapat 4 platform yang berada di puncak media sosial dan marketing yaitu Instagram, TikTok, Facebook, dan YouTube. 
                Namun, kedua data yang telah ditunjukkan berasal dari global dan Amerika Serikat, sehingga masih
                diperlukan analisis kondisi terhadap trend di Indonesia sebagai insight yang lebih relevan.
                </p>''', unsafe_allow_html=True)

    # Analisis Google Trends

    st.markdown("---")
    st.subheader("Analisis Trend Google Search  di Indonesia")

    media = df_media[['media','value']].set_index('media')

    capt1, cht1 = st.columns([1, 4])
    with capt1:
        freq = st.selectbox("Pilih Tampilan Data", ('Mingguan', 'Bulanan', 'Tahunan'))
        if freq == 'Mingguan':
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('W').sum()
        elif freq == 'Bulanan':
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('M').sum()
        else:
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('Y').sum()
        st.dataframe(trends, height=350)
    with cht1 :
        if freq == 'Mingguan':
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('W').sum()
        elif freq == 'Bulanan':
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('M').sum()
        else:
            trends = df[['Week','YouTube','TikTok','Instagram','Facebook']].set_index('Week').resample('Y').sum()
        fig = px.line(trends)

        fig.update_layout(
            hovermode='x unified',
            updatemenus=[
                dict(
                    type = "buttons",
                    direction = "left",
                    buttons=list([
                        dict(
                            args=[{"yaxis.type": "linear"}],
                            label="LINEAR",
                            method="relayout"
                        ),
                        dict(
                            args=[{"yaxis.type": "log"}],
                            label="LOG",
                            method="relayout"
                        )
                    ]),
                ),
            ]
        )
        fig.update_layout(xaxis_title="Tanggal", yaxis_title="Trend Google Search (0-100)")
        st.plotly_chart(fig, use_container_width=True)

    met1, met2, met3, met4 = st.columns([1,1,1,1])
    # Metrics
    with met3:
        st.metric("TikTok", "82", "8200%")
    with met1:
        st.metric("YouTube", "59","-18%")
    with met2:
        st.metric("Instagram", "39")
    with met4:
        st.metric("Facebook", "42","-45%")
    st.markdown('''<p class="big-font">
                Terdapat beberapa detil menarik yang dapat disimpulkan dari data di atas: TikTok dalam kurun waktu dua tahun
                telah menjadi media sosial paling "trendy" di Google; Sedangkan, media sosial yang telah lama menjadi
                bagian dari kehidupan internet Indonesia seperti Facebook dan YouTube, telah mengalami penurunan dari masa ke masa.
                Tahap selanjutnya adalah untuk mencari tahu sebaran umur para pembentuk "trend" dan pandangan
                publik terhadap media sosial tersebut untuk menemukan benang merah dari permasalahan ini. </p>''', unsafe_allow_html=True)


    st.markdown("---")
    st.subheader('Analisis Demografi dan Sentimen Publik')

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["YouTube", "Instagram", "TikTok","Facebook","Summary Demografi Umur"])
    with tab1:
        yt1, yt2, yt3 = st.columns([1,1,1])
        with yt1:
            fig5 = go.Figure(data=[
            go.Bar(name='Female', x=de_youtube['age'], y=de_youtube['female']),
            go.Bar(name='Male', x=de_youtube['age'], y=de_youtube['male'])
            ])
            fig5.update_layout(barmode='group',title_text = 'Data Demografik Umur YouTube (%)', title_x = 0.5,xaxis_title="Kelompok Umur", yaxis_title="Persentase dari Total User (%)")
            st.plotly_chart(fig5, use_container_width=True)
        with yt2:
            st.markdown("""YouTube tidak hanya berfungsi sebagai media sosial untuk tujuan hiburan/rekreasi,
                    melainkan tempat bagi orang-orang yang memiliki pertanyaan tentang hal apapun
                    dan sedang mencari jawaban. Pertanyaan-pertanyaan tersebut dapat datang
                    dari kalangan umur mana saja, mulai dari remaja yang mencari tips and tricks untuk
                    hobi yang dimiliki sampai orang tua yang baru belajar memakai
                    internet. Hal tersebut dicerminkan oleh pemetaan demografi umur yang relatif
                    merata dengan lonjakan di umur efektif bekerja.""")
            st.markdown('---')
            st.markdown("""
                    Sentimen publik terhadap YouTube mayoritas bersifat positif dengan perbandingan 3:1 terhadap
                    sentimen negatif. Data tersebut menunjukkan bahwa
                    YouTube tidak hanya salah satu media sosial yang telah lama terbangun,
                    tetapi memiliki sentimen publik yang merasa diberikan manfaat olehnya. Hal ini
                    dapat memberikan dorongan lebih untuk kepastian keberadaan market di YouTube.""")
        with yt3:
            sayoutube = px.pie(
                data_frame = pie_sayoutube,
                values = 'value',
                names = 'sentiment',
                color = 'sentiment',
                color_discrete_map= {'Positive':'green','Negative':'red','Neutral':'light blue'},
                template = 'presentation',
                width = 1000,
                height = 500,
                hole = 0.3
            )
            sayoutube.update_traces(textposition='outside',textinfo='percent+label',
            marker=dict(line=dict(color='#000000',width=4)),
            pull=[0.2,0,0],opacity=0.7,rotation=230)
            sayoutube.update_layout(showlegend=False,title_text='Sentiment Analysis: YouTube')
            st.plotly_chart(sayoutube, use_container_width=True)

    with tab2:
        ig1, ig2, ig3 = st.columns([1,1,1])
        with ig1:
            fig4 = go.Figure(data=[
            go.Bar(name='Female', x=de_instagram['age'], y=de_instagram['female']),
            go.Bar(name='Male', x=de_instagram['age'], y=de_instagram['male'])
            ])
            fig4.update_layout(barmode='group',title_text = 'Data Demografik Umur Instagram (%)', title_x = 0.5,xaxis_title="Kelompok Umur", yaxis_title="Persentase dari Total User (%)")
            st.plotly_chart(fig4, use_container_width=True)
        with ig2:
            st.markdown("""Instagram berfokus dalam mem-posting foto dan video, dengan tujuan
                        bagi user agar dapat membagikan momen-momen dalam hidupnya kepada orang lain. 
                        Dengan tujuan tersebut, tidak heran bagi demografi umur
                        pemakai instagram kalau mayoritas berada di umur perkuliahan dan awal kerja.
                        Range umur tersebut merupakan puncak dari fase networking dan eksplorasi diri
                        menyebabkan terdapat jauh lebih banyak cerita yang dapat dibagikan.""")
            st.markdown('---')
            st.markdown("""Pandangan publik terhadap instagram relatif netral dengan perbandingan 2.3 : 1
                        untuk positif dan negatif. Dengan ekosistem sosial instagram, orang-orang
                        tidak akan mudah merasa dirugikan dengan melihat foto/menonton video
                        dari seseorang yang mereka follow. Hal yang perlu digaris bawahi dalam instagram
                        ini adalah andil para influencer yang diikuti, memiliki
                        kemungkinan yang besar untuk menyukseskan marketing terhadap para followers.""")
        with ig3:
            sainstagram = px.pie(
                data_frame = pie_sainstagram,
                values = 'value',
                names = 'sentiment',
                color = 'sentiment',
                color_discrete_map= {'Positive':'green','Negative':'red','Neutral':'light blue'},
                title = 'Sentiment Analysis: Instagram',
                template = 'presentation',
                width = 1000,
                height = 500,
                hole = 0.3
                )
            sainstagram.update_traces(textposition='outside',textinfo='percent+label',
            marker=dict(line=dict(color='#000000',width=4)),
            pull=[0,0.2,0],opacity=0.7,rotation=0)
            sainstagram.update_layout(showlegend=False)
            
            st.plotly_chart(sainstagram, use_container_width=True)

    with tab3:
        tk1, tk2, tk3 = st.columns([1,1,1])
        with tk1:
            fig6 = go.Figure([go.Bar(name='Percentage', x=de_tiktok['age'], y=de_tiktok['value'])])
            fig6.update_layout(title_text = 'Data Demografik Umur TikTok (%)', title_x = 0.5,xaxis_title="Kelompok Umur", yaxis_title="Persentase dari Total User (%)")
            st.plotly_chart(fig6, use_container_width=True)
        with tk2:
            st.markdown("""TikTok, media sosial termuda dari empat yang dibahas, merupakan tempat bagi
                        siapapun untuk mem-posting video pendek yang dapat dipersonalisasi seekspresif
                        mungkin. Kunci dari kesuksesan platform TikTok adalah berasal dari satu kata,
                        "Trends". Tren di tiktok dapat ditemukan dalam berbagai bentuk: challenge,
                        musik, dance, dll. Hal tersebut menggaet banyak anak kecil dan remaja untuk
                        mengikuti platform TikTok dan sangat sedikit orang usia tua yang tertarik menggunakannya.""")
            st.markdown('---')
            st.markdown("""Dengan perbandingan 1.6 : 1 untuk pandangan positif dan negatif publik, 
                        mencerminkan bahwa TikTok belum mendapatkan
                        pandangan yang baik dari publik secara keseluruhan. Dengan usia aplikasi TikTok 
                        yang relatif muda yaitu 6 tahun, ditambah dengan demografi umur
                        yang bermayoritas pada kalangan remaja membuat sentimen publik terhadap tiktok
                        yang paling rendah dari keempat media sosial.""")
        with tk3:
            satiktok = px.pie(
                data_frame = pie_satiktok,
                values = 'value',
                names = 'sentiment',
                color = 'sentiment',
                color_discrete_map= {'Positive':'green','Negative':'red','Neutral':'light blue'},
                title = 'Sentiment Analysis: TikTok',
                template = 'presentation',
                width = 1000,
                height = 500,
                hole = 0.3
            )
            satiktok.update_traces(textposition='outside',textinfo='percent+label',
            marker=dict(line=dict(color='#000000',width=4)),
            pull=[0,0.2,0],opacity=0.7,rotation=0)
            satiktok.update_layout(showlegend=False)
            st.plotly_chart(satiktok, use_container_width=True)

    with tab4:
        fb1, fb2, fb3 = st.columns([1,1,1])
        with fb1:
            fig6 = go.Figure([go.Bar(name='Percentage', x=de_facebook['age'], y=de_facebook['value'])])
            fig6.update_layout(title_text = 'Data Demografik Umur Facebook (%)', title_x = 0.5,xaxis_title="Kelompok Umur", yaxis_title="Persentase dari Total User (%)")
            st.plotly_chart(fig6, use_container_width=True)
        with fb2:
            st.markdown("""Facebook adalah media sosial yang paling bersinonim dengan aktivitas internet
                        warga Indonesia selama ini berdasarkan data.  Selain foto dan video, user dapat membagikan
                        artikel-artikel, opini, dan pekerjaan yang dilakukan. Facebook juga memiliki fitur untuk
                        membangun komunitas dan mendorong aktivitas networking,
                        baik lingkup personal sampai profesional. Dengan jumlah user terbanyak dari keempat
                        media sosial, demografi umur Facebook mayoritas berada di usia perkuliahan
                        dan profesional bekerja.""")
            st.markdown('---')
            st.markdown("""Dengan perbandingan 3 : 1 untuk sentimen positif dan negatif, Facebook merupakan
                        media sosial yang paling menimbulkan opini positif. Sejak awal didirikan, Facebook
                        selalu dinilai membawa banyak manfaat bagi para user untuk melakukan kehidupan
                        sehari-hari dalam konteks online. Sentimen positif ini tentunya mendorong kepastian
                        terhadap Facebook sebagai platform untuk marketing. """)
        with fb3:
            safacebook = px.pie(
                data_frame = pie_safacebook,
                values = 'value',
                names = 'sentiment',
                color = 'sentiment',
                color_discrete_map= {'Positive':'green','Negative':'red','Neutral':'light blue'},
                title = 'Sentiment Analysis: Facebook',
                template = 'presentation',
                width = 1000,
                height = 500,
                hole = 0.3
            )
            safacebook.update_traces(textposition='outside',textinfo='percent+label',
            marker=dict(line=dict(color='#000000',width=4)),
            pull=[0.2,0,0],opacity=0.7,rotation=220)
            safacebook.update_layout(showlegend=False)
            st.plotly_chart(safacebook, use_container_width=True)
    
        with tab5:
            fig5 = go.Figure(data=[
            go.Bar(name='YouTube', y=de_all['YouTube'], x=de_all['age'], orientation='v'),
            go.Bar(name='Instagram', y=de_all['Instagram'], x=de_all['age'], orientation='v'),
            go.Bar(name='TikTok', y=de_all['TikTok'], x=de_all['age'], orientation='v'),
            go.Bar(name='Facebook', y=de_all['Facebook'], x=de_all['age'], orientation='v')
            ])
            fig5.update_layout(barmode='group',xaxis_title="Kelompok Umur", yaxis_title="Persentase dari Total User (%)")
            st.plotly_chart(fig5, use_container_width=True)

    st.markdown("---")

    st.subheader('Rekomendasi berdasarkan Analisis')
    st.write("""Pandangan terhadap topik ini menjadi lebih objektif setelah mendapatkan 
            analisis terhadap keempat media sosial dari sisi tren, demografi umur, dan sentimen publik.
            Proses analisis masih dapat dilengkapi dengan memperhitungkan variabel yaitu bentuk
            dari konten marketing itu sendiri. Secara umum, para marketer berpendapat bahwa
            konten dapat dibedakan menjadi Image dan Video, kedua hal tersebut merupakan tulang
            punggung dari media sosial sehingga kita dapat menemukan hubungannya. Untuk menganalisis
            konten seperti apa yang paling menggambarkan suatu media sosial, kita dapat melakukan Twitter
            web scraping dengan kata kunci yakni nama media sosial tersebut, lalu dikemas dengan visualisasi dalam bentuk word cloud. 
            """)
    st.markdown('---')
    st.write("""Sebagai kesimpulan sekaligus rekomendasi dari analisis yang telah dilakukan, saya persilakan anda, seorang marketer,
            untuk memilih opsi yang sesuai untuk produk anda.""")
    op2, op3 = st.columns([1,1])
    with op2:
        st.session_state['demography'] = st.selectbox('Sebaran umur',['...','13-17','18-34','35+'])
    with op3:
        st.session_state['content'] = st.selectbox('Rencana konten',['...','Image','Video'])

    if st.session_state['demography'] == '13-17' and  st.session_state['content'] =='Image':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi1:
            wc_yt = st.image(Image.open("wc_instagram.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik Instagram')
        with opsi2:
            st.write("""Melalui analisis tweets menggunakan TwitterAPI, kata-kata yang paling sering
                    menemani tweets bertopik Instagram antara lain: foto, posted, dan follower.
                    Seperti yang telah dibahas, fitur utama dari Instagram berpacu kepada mem-post
                    foto dan video. Dari foto dan video tersebut, para user akan senantiasa membahas
                    atau menyebarkan info tentang hal-hal menarik yang ditemukan melalui
                    fitur Instagram Stories.""")
            st.markdown ('---')
            st.write("""Selain fitur Instagram Stories, marketing melalui post biasa juga sangat memungkinkan,
                    dengan fitur highlighting product pada sebuah post membuat reach semakin mudah bagi para
                    user. Terdapat pula opsi advertisement secara konvensional yaitu promotion pada home page
                    Instagram, dengan menggunakan metode ini produk bisa lebih tepat sasaran dengan menyelaraskan
                    sesuai algoritma para user sebelum menampilkan iklan tersebut.""")

                    
        with opsi3:
            st.write("""Bagi kalangan remaja awal, Instagram merupakan media sosial terpopuler nomor
                    dua.Dengan konten marketing yang berbentuk foto/statis, Instagram 
                    merupakan platform yang lebih tepat dibandingkan TikTok. Ditambah dengan
                    fitur-fitur marketing yang dimiliki oleh Instagram seperti detil
                    demografi followers, pemetaan traffic paling tinggi untuk posts, dan
                    algoritma hashtags akan sangat membantu dalam penyusunan strategi.""")
            st.markdown ('---')
            st.write("""Memperluas jaringan marketing dengan membayar influencer-influencer
                    yang memiliki fanbase tertentu, memiliki kemungkinan yang besar untuk
                    berhasil. YouGov mengatakan bahwa 2 dari 3 remaja telah mem-follow seorang
                    influencer dari bidang yang mereka minati. Sebanyak 49% konsumen di Instagram 
                    bertumpu kepada rekomendasi influencers untuk pembelian produk, 
                    diikuti dengan 40% konsumen telah membeli sesuatu setelah melihatnya 
                    di Instagram (Digital Marketing Insitute).""")

    if st.session_state['demography'] == '13-17' and  st.session_state['content'] =='Video':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi1:
            wc_tk = st.image(Image.open("wc_tiktok.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik TikTok')
        with opsi2:
            st.write("""For You Page (FYP) adalah fitur TikTok yang berisi rekomendasi video TikTok berdasarkan 
            sejumlah faktor seperti riwayat video yang telah dilihat, dikomen, dan disukai oleh pengguna tersebut. FYP 
            muncul di dalam word cloud tentang TikTok, membuktikan bahwa fitur tersebut menjadi inti dari TikTok itu sendiri. 
            Untuk menjadi creator FYP, dibutuhkan modal seperti mengupload konten yang konsisten dan penonton yang cukup banyak.""")
            st.markdown ('---')
            st.write("""TikTok menawarkan format periklanan diantaranya "In-feed Ads" dan "Spark Ads". "In-feed ads" adalah post 
            iklan menggunakan video/foto yang akan muncul di fitur For You Page pengguna, dengan demikian memberikan kesempatan agar 
            pengguna bisa berinteraksi dengan post tersebut. Sedangkan, "Spark Ads" adalah fitur pengiklanan di TikTok yang mendorong 
            konten tersebut untuk lebih sering muncul di For You Page dibandingkan dengan "In-feed ads".""")
        with opsi3:
            st.write("""TikTok memiliki sebaran di usia yakni 13-17 paling tinggi. Dengan sebaran demografi tersebut, 
            marketing yang ditargetkan untuk usia remaja awal cocok dilakukan di platform media sosial ini. TikTok
            memiliki banyak metode untuk menarik perhatian pengguna, seperti challenges, audio atau video yang sedang trending, 
            juga pemanfaat influencer atau brand ambassador membuat TikTok menjadi platform marketing yang fleksibel.""")
            st.markdown('---')
            st.write("""Dalam perkembangannya, TikTok telah menyalurkan 1 miliar dollar AS untuk membentuk 
            "TikTok Creator Fund", sebuah pendanaan bagi creator yang memenuhi syarat. Para creator tersebut diharapkan menarik 
            lebih banyak brand pratnership, sponsorship, dan representation deal. Dengan tren penggunaan influencer sebagai channel 
            social media marketing yang semakin naik, saya menyarankan anda sebagai digital marketer untuk memanfaatkan tren tersebut.""")

    if st.session_state['demography'] == '18-34' and  st.session_state['content'] =='Image':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi1:
            wc_ig = st.image(Image.open("wc_instagram.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik Instagram')
        with opsi2:
            st.write("""Instagram memiliki beberapa jenis iklan, antara lain "Instagram Stories" dan "Reels" yang dapat mendukung penempatan feed dimensi foto dan video, artinya Anda dapat mengunggah satu foto atau video hingga 120 detik. Selain itu, Instagram Shop dimana iklan dapat dalam format image tunggal, carousel, atau koleksi. Semua iklan akan muncul sebagai gambar persegi 1:1 dan dapat diketuk ke halaman detail produk situs web.

Dalam grafik demografinya, pengguna Instagram didominasi oleh umur 18-24 tahun. Marketer yang mencari platform untuk membuat iklan dapat menggunakan platform Instagram untuk memikat range demografi yang diinginkan secara lebih efektif. Sementara itu, dengan persebaran demografi yang didominasi oleh kelompok umur 25-34, Facebook menjadi yang terdepan untuk marketing kepada target market tersebut. 

Facebook ads terdapat beberapa jenis antara lain: "Collection ads" yang bersifat dinamis kami untuk menampilkan produk dengan berbagai cara. Lalu ada "Carousel ads" yang dapat menampilkan hingga sepuluh gambar atau video dalam satu iklan, masing-masing dengan tautannya sendiri.""")
        with opsi3:
            wc_fb = st.image(Image.open("wc_facebook.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik Facebook')

    if st.session_state['demography'] == '18-34' and  st.session_state['content'] =='Video':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi1:
            wc_tk = st.image(Image.open("wc_tiktok.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik TikTok')
        with opsi2:
            st.write("""Advertising di platform TikTok paling umum dapat dilakukan dengan In-feed Ads, Spark Ads, dan Brand Takeover Ads. In-feed ads adalah post iklan menggunakan video/foto yang akan muncul di fitur For You Page pengguna, dengan demikian memberikan kesempatan agar pengguna bisa berinteraksi dengan post tersebut. Spark Ads adalah salah satu fitur pengiklanan di TikTok yang mendorong konten tersebut untuk lebih sering muncul di For You Page, dapat meningkatkan hingga 142% enggagement rate dalam penggunaannya.

Grafik demografi TikTok menunjukkan bahwa pengguna TikTok didominasi oleh range usia 18-24 tahun. Dengan demikian, penggunaan TikTok sebagai platform marketing efektif untuk digunakan saat menyasar kalangan dewasa awal. Sementara itu, platform YouTube memiliki demografi yang tinggi pada sebaran umur 25-34 tahun, menjadikan platform tersebut efektif untuk digunakan sebagai media marketing yang menyasar kalangan tersebut.


Dalam pengiklanan, YouTube memberikan banyak pilihan format. Format tersebut adalah: Skippable video ads, Non-skippable video ads, Bumper Ads, dan Overlay ads. Secara garis besar, Skippable ads adalah iklan yang dapat diskip setelah 5 detik, sementara non-skippable ads tidak dapat diskip. Bumper adalah iklan yang harus ditonton sebelum menonton video yang dituju, dan overlay adalah iklan yang muncul selagi video yang dituju berjalan. Semua format iklan dapat muncul di semua device kecuali overlay yang hanya dapat muncul di komputer atau PC.""")
        with opsi3:
            wc_yt = st.image(Image.open("wc_youtube.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik YouTube')

    if st.session_state['demography'] == '35+' and  st.session_state['content'] =='Image':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi3:
            wc_fb = st.image(Image.open("wc_facebook.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik Facebook')
        with opsi2:
            st.write("""Dengan melakukan Twitter Web Scraping, kita dapat menemukan kata-kata
                    yang berkaitan erat dengan peran Facebook di mata publik. Kata-kata seperti
                    "People", "Page", dan nama-nama media sosial lainnya sangat sering muncul.
                    Facebook dapat dianggap sebagai pusat dari segala hal berbau internet,
                    tempat di mana kita bisa mengikuti bidang yang kita minati tetapi
                    juga membangun persona yang tergolong profesional. Banyak
                    komunitas yang telah membangun page di Facebook sebagai media utama
                    networking.""")
            st.markdown ('---')
            st.write("""Facebook memiliki banyak fitur yang memfasilitasi pembangunan koneksi
                        antara satu user dengan yang lain. Selain itu, dengan kemampuan kita
                        untuk membagikan artikel/berita tentang apapun dari sumber manapun
                        di Internet menjadikan Facebook sebuah media sosial yang serba bisa.""")

        with opsi1:
            st.write("""Kelebihan dari Facebook sebagai media sosial di Indonesia adalah
                    keberadaannya yang tergolong lebih tua/lama dibandingkan media-media
                    sosial lainnya, sehingga sudah tidak asing dengan orang-orang pekerja dan
                    orang tua. Hal tersebut tercerminkan dari sebaran demografi umur yang
                    cukup konsisten dalam umur 35 ke atas. Menurut survey, orang tua
                    memiliki ketertarikan untuk memakai Facebook atas alasan: ikatan sosial, 
                    rasa ingin tahu, dan menanggapi permintaan anggota keluarga (Science Direct).""")
            st.markdown ('---')
            st.write("""Dalam menghadapi market yang luas untuk range usia 35 ke atas, Facebook
                    menyediakan banyak fasilitas untuk memudahkan pengiklanan sebuah produk.
                    Iklan tersebut dapat diunggah dalam bentuk foto ataupun video, dengan
                    format seperti "Carousel ads" yang berbentuk tampilan sebanyak
                    sepuluh slides dan "Collection ads" yang bersifat lebih dinamis.""")

    if st.session_state['demography'] == '35+' and  st.session_state['content'] =='Video':
        opsi1, opsi2, opsi3 = st.columns([1,1,1])
        with opsi3:
            wc_yt = st.image(Image.open("wc_youtube.png"), caption = 'Frekuensi kata-kata dalam tweet bertopik YouTube')
        with opsi2:
            st.write("""YouTube merupakan salah satu platform utama dalam mencari berbagai informasi dan hiburan.
            Dalam word cloud, dapat kita lihat kata "Stream", stream atau live stream adalah metode penyaluran media dengan real 
            time dari creator ke penonton. Dengan jumlah penonton stabil, youtuber menjadi sasaran marketer untuk mempromosikan produknya
            dengan cara sponsorship. Sponsorship ini dapat dilakukan dengan kedua Live Stream dan Konten Video youtube secara umum.""")
            st.markdown ('---')
            st.write("""Terdapat 4 pilihan format pengiklanan yang ditawarkan oleh Youtube. Format tersebut adalah: 
            Skippable video ads, Non-skippable video ads, Bumper Ads, dan Overlay ads. Secara umum, Skippable ads adalah iklan 
            yang dapat diskip setelah 5 detik, sementara non-skippable ads tidak dapat diskip. Bumper adalah iklan yang harus ditonton 
            sebelum menonton video yang dituju, dan overlay adalah iklan yang muncul selagi video yang diputar berjalan.""")
        with opsi1:
            st.write("""Youtube menjadi salah satu platform yang bermanfaat bagi semua umur, mulai dari video kartun anak kecil 
            hingga video mengenai teknologi terbaru, semuanya berada dalam satu platform. Dengan persebaran umur yang hampir merata, 
            YouTube dapat menjadi andalan marketer yang menargetkan audiens dengan range umur yang besar.
            Dengan range konsumen yang luas, pastinya terdapat banyak content creator di YouTube untuk mengisi demand tersebut.""")
            st.markdown ('---')
            st.write("""Sponsorship dengan creator dan youtuber di platform ini memberikan sudut pandang baru mengenai 
            produk yang akan anda promosikan. Pada statistik yang dilaksanakan oleh Digital Marketing Institute, 
            ditemukan bahwa 42% pengguna internet menggunakan teknologi Ad-blocking, dan YouTube juga ikut terkena imbasnya. 
            Salah satu kunci untuk mengatasi hal itu adalah dengan bekerja sama dengan youtuber untuk membentuk sponsorship, marketing deal,
            bahkan kampanye.""")

if page == 'Documentation':
    st.markdown('''<p class="big-font">What tools were used in the making of this project?</p>''', unsafe_allow_html=True)
    st.markdown('* Python in Data collecting')
    st.markdown('* MySQL, Ms.Excel, and Python in Data Processing and Cleaning')
    st.markdown('* Python in Data Visualization')
    st.markdown('''<p class="big-font">Where can we see the sentiment analysis that was done?</p>''', unsafe_allow_html=True)
    with st.expander("Sentiment Analysis Dataframes"):
        sa1,sa2,sa3,sa4 = st.columns([1,1,1,1])
        with sa3:
            st.dataframe(df_tiktok)
        with sa2:
            st.dataframe(df_facebook)
        with sa4:
            st.dataframe(df_sainstagram)
        with sa1:
            st.dataframe(df_youtube)
    st.markdown('''<p class="big-font">What were the data sources for this project?</p>''', unsafe_allow_html=True)
    with st.expander("Data source"):
        st.markdown("1. TwitterAPI Web Scraping")
        st.markdown("2. https://trends.google.co.id/trends/explore?date=today%205-y&geo=ID&q=youtube,%2Fg%2F11f555cn8l,instagram,facebook")
        st.markdown("3. https://www.searchenginejournal.com/social-media/biggest-social-media-sites/")
        st.markdown("4. https://www.statista.com/statistics/248769/age-distribution-of-worldwide-instagram-users/")
        st.markdown("5. https://blog.hootsuite.com/youtube-stats-marketers/")
        st.markdown("6. https://id.oberlo.com/statistics/tiktok-age-demographics")
    st.markdown('''<p class="big-font">Closing Statement</p>''', unsafe_allow_html=True)
    st.write("""This has been my capstone project for Tetris Program, I am well aware that i have not taken into account many more variables
            such as marketing budget. Even then, i still hope that this project has given the audience a few insights and might assist
            in future analyses. If you have any questions please feel free to contact me as seen on the contact page!""")
    st.write("Thank you for your attention.")

if page == 'Contact':
    st.image('banner.png')
    link1,link2,link3,link4 = st.columns([1,1,1,1])
    with link3:
        st.markdown(
            "[![this is an image link](https://i.ibb.co/94mNmwj/2.png)](https://mail.google.com/)"
        )
    with link1:
        st.markdown(
            "[![this is an image link](https://i.ibb.co/WDRmsyq/1.png)](https://www.linkedin.com/in/m-ryan-rahmadifa/)"
        )
    link1,link2,link3,link4 = st.columns([1,1,1,1])
    with link1:
        st.markdown(
            "[![this is an image link](https://i.ibb.co/t8T9X1V/3.png)](https://www.instagram.com/ryanrahmadifa/)"
        ) 
    with link3:
        st.markdown(
            "[![this is an image link](https://i.ibb.co/nBrPDnn/4.png)](https://line.me/en/)"
        )
