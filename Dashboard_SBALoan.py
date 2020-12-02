# Flask : library utama untuk membuat API
# render_template : agar dapat memberikan respon file html
# request : untuk membaca data yang diterima saat request datang
from flask import Flask, render_template, request
# plotly dan plotly.graph_objs : membuat plot
import plotly
import plotly.graph_objs as go
# pandas : untuk membaca csv dan men-generate dataframe
import pandas as pd
import json
from sqlalchemy import create_engine

## Joblib untuk Load Model
import joblib

# print('Import succes')

# untuk membuat route
app = Flask(__name__)

## IMPORT DATA USING pd.read_csv
sba = pd.read_csv('./static/SBA_Loan_Sample.csv')

# category plot function
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'LowDoc', cat_y = 'DisbursementGross',
    estimator = 'count', hue = 'RevLineCr'):

    # generate dataframe tips.csv
    sba = pd.read_csv('./static/SBA_Loan_Sample.csv')

    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in sba[hue].unique():
            hist = go.Histogram(
                x=sba[sba[hue]==val][cat_x],
                y=sba[sba[hue]==val][cat_y],
                histfunc=estimator,
                name=val
            )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Histogram'
    elif cat_plot == 'boxplot':
        data = []

        for val in sba[hue].unique():
            box = go.Box(
                x=sba[sba[hue] == val][cat_x], #series
                y=sba[sba[hue] == val][cat_y],
                name = val
            )
            data.append(box)
        title='Box'
    # menyiapkan config layout tempat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='Small Business'),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    #json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# akses halaman menuju route '/' untuk men-test
# apakah API sudah running atau belum
@app.route('/')
def index():

    plot = category_plot()
    # dropdown menu
    # kita lihat pada halaman dashboard terdapat menu dropdown
    # terdapat lima menu dropdown, sehingga kita mengirimkan kelima variable di bawah ini
    # kita mengirimnya dalam bentuk list agar mudah mengolahnya di halaman html menggunakan looping
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]
    list_y = [('DisbursementGross', 'DisbursementGross'), ('Term', 'Term'), ('Portion', 'Portion')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]


    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot='histplot',
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x='RevLineCr',

        # untuk sumbu Y tidak ada, nantinya menu dropdown Y akan di disable
        # karena pada histogram, sumbu Y akan menunjukkan kuantitas data

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator='count',
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue='RevLineCr',
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue)
# ada dua kondisi di mana kita akan melakukan request terhadap route ini
# pertama saat klik menu tab (Histogram & Box)
# kedua saat mengirim form (saat merubah salah satu dropdown) 
@app.route('/cat_fn/<nav>')
def cat_fn(nav):

    # saat klik menu navigasi
    if nav == 'True':
        cat_plot = 'histplot'
        cat_x = 'LowDoc'
        cat_y = 'DisbursementGross'
        estimator = 'count'
        hue = 'RevLineCr'
    
    # saat memilih value dari form
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    # Dari boxplot ke histogram akan None
    if estimator == None:
        estimator = 'count'
    
    # Saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'DisbursementGross'

    # Dropdown menu
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [ ('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]
    list_y = [('DisbursementGross', 'DisbursementGross'), ('Term', 'Term'), ('Portion', 'Portion')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
    )

##################
## SCATTER PLOT ##
##################

# scatter plot function
def scatter_plot(cat_x, cat_y, hue):


    data = []

    for val in sba[hue].unique():
        scatt = go.Scatter(
            x = sba[sba[hue] == val][cat_x],
            y = sba[sba[hue] == val][cat_y],
            mode = 'markers',
            name = val
        )
        data.append(scatt)

    layout = go.Layout(
        title= 'Scatter',
        title_x= 0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/scatt_fn')
def scatt_fn():
    cat_x = request.args.get('cat_x')
    cat_y = request.args.get('cat_y')
    hue = request.args.get('hue')

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'Term'
        cat_y = 'Portion'
        hue = 'LowDoc'

    # Dropdown menu
    list_x = [('GrAppv', 'GrAppv'), ('Term', 'Term'), ('Portion', 'Portion')]
    list_y = [('GrAppv', 'GrAppv'), ('Term', 'Term'), ('Portion', 'Portion')]
    list_hue = [('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]

    plot = scatter_plot(cat_x, cat_y, hue)

    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x= list_x,
        drop_y= list_y,
        drop_hue= list_hue
    )

##############
## PIE PLOT ##
##############

def pie_plot(hue = 'sameState'):
    


    vcounts = sba[hue].value_counts()

    labels = []
    values = []

    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])
    
    data = [
        go.Pie(
            labels=labels,
            values=values
        )
    ]

    layout = go.Layout(title='Pie', title_x= 0.48)

    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')

    if hue == None:
        hue = 'sameState'

    list_hue = [('sameState', 'sameState'), ('UrbanRural', 'Urban Rural'), ('RevLineCr', 'RevLineCr'), ('LowDoc', 'Low Doc'), ('MIS_Status', 'Status'), ('sector', 'NAICS')]

    plot = pie_plot(hue)
    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue= list_hue)

## Predict page
@app.route('/pred_lr')
def pred_lr():
    sba = pd.read_csv('./static/SBA_Loan_Sample.csv').head(50)
    sba.index.name = None
    titles = "-"
    return render_template('predict.html', tables = [sba.to_html(classes = 'data', header='true')], titles=titles)




## Result
@app.route('/pred_result', methods=['POST', 'GET'])
def pred_result():

    if request.method == 'POST':
    ## Untuk Predict
        input = request.form

        Term=int(input['Term'])

        UrbanRural = int(input['UrbanRural'])
        
        isFranchise = ''
        if input['isFranchise'] == 'Franchise':
            isFranchise = 1
        else:
            isFranchise = 0

        GrAppv = float(input['GrAppv'])
        
        
        sector__Accommodation_food_serv = 0
        sector__Admini_sup_and_waste_mgm_rem = 0
        sector__Ag_fores_ﬁshi_hunting = 0
        sector__Arts_enter_recreation = 0
        sector__Construction = 0
        sector__Educational_services = 0
        sector__Finance_insurance = 0
        sector__Health_care_social_ass = 0
        sector__Information = 0
        sector__Management_and_enterprises = 0
        sector__Manufacturing = 0
        sector__Mining_quar_oil_gas_ext = 0
        sector__Other_no_pub = 0
        sector__Prof_scien_and_tech_serv = 0
        sector__Public_admin = 0
        sector__RE_rental_leasing = 0
        sector__Retail_trade = 0
        sector__Trans_Ware = 0
        sector__Utilities = 0
        sector__Wholesale_trade = 0

        if input['sector'] == 'Ag_fores_ﬁshi_hunting':
            sector__Ag_fores_ﬁshi_hunting += 1
        elif input['sector'] == 'Mining_quar_oil_gas_ext':
            sector__Mining_quar_oil_gas_ext +=1
        elif input['sector'] == 'Utilities':
            sector__Utilities +=1
        elif input['sector'] == 'Construction':
            sector__Construction +=1
        elif input['sector'] == 'Wholesale_trade':
            sector__Wholesale_trade +=1
        elif input['sector'] == 'Retail_trade':
            sector__Retail_trade +=1
        elif input['sector'] == 'Trans_&_Ware':
            sector__Trans_Ware +=1
        elif input['sector'] == 'Information':
            sector__Information +=1
        elif input['sector'] == 'Finance_insurance':
            sector__Finance_insurance  +=1
        elif input['sector'] == 'RE_rental_leasing':
            sector__RE_rental_leasing +=1
        elif input['sector'] == 'Prof_scien_and_tech_serv':
            sector__Prof_scien_and_tech_serv +=1
        elif input['sector'] == 'Management_and_enterprises':
            sector__Management_and_enterprises +=1
        elif input['sector'] == 'Admini_sup_and_waste_mgm_rem':
            sector__Admini_sup_and_waste_mgm_rem +=1
        elif input['sector'] == 'Educational_services':
            sector__Educational_services +=1
        elif input['sector'] == 'Health_care_social_ass':
            sector__Health_care_social_ass +=1
        elif input['sector'] == 'Arts_enter_recreation':
            sector__Arts_enter_recreation +=1
        elif input['sector'] == 'Accommodation_food_serv':
             sector__Accommodation_food_serv +=1
        elif input['sector'] == 'Other_no_pub ':
             sector__Other_no_pub +=1
        elif input['sector'] == 'Public_admin':
            sector__Public_admin +=1
        elif input['sector'] == 'Manufacturing':
            sector__Manufacturing +=1

        sameState = int(input['sameState'])
        NoEmp = int(input['NoEmp'])

        feature = (Term, NoEmp, UrbanRural, GrAppv, isFranchise,
        sameState, sector__Accommodation_food_serv, sector__Admini_sup_and_waste_mgm_rem,
        sector__Ag_fores_ﬁshi_hunting, sector__Arts_enter_recreation, sector__Construction, sector__Educational_services,
        sector__Finance_insurance, sector__Health_care_social_ass, sector__Information, sector__Management_and_enterprises, 
        sector__Manufacturing, sector__Mining_quar_oil_gas_ext, sector__Other_no_pub, sector__Prof_scien_and_tech_serv,
        sector__Public_admin, sector__RE_rental_leasing, sector__Retail_trade, sector__Trans_Ware, sector__Utilities,
        sector__Wholesale_trade)

        data = pd.DataFrame(data=feature, index=['Term', 'NoEmp', 'UrbanRural', 'GrAppv', 'isFranchise', 'sameState', 'sector__Accommodation_food_serv', 'sector__Admini_sup_and_waste_mgm_rem', 'sector__Ag_fores_ﬁshi_hunting', 'sector__Arts_enter_recreation', 'sector__Construction', 'sector__Educational_services', 'sector__Finance_insurance', 'sector__Health_care_social_ass', 'sector__Information', 'sector__Management_and_enterprises', 'sector__Manufacturing', 'sector__Mining_quar_oil_gas_ext', 'sector__Other_no_pub', 'sector__Prof_scien_and_tech_serv', 'sector__Public_admin', 'sector__RE_rental_leasing', 'sector__Retail_trade', 'sector__Trans_Ware', 'sector__Utilities', 'sector__Wholesale_trade']).T

        pred = model.predict(data)[0]
        pred_proba = model.predict_proba(data)
        hasil = (pred_proba[0][1]*100).round(2)
        result = f'Probabilitas of Small Business will be Default :{hasil}%'

        ## Untuk Isi Data
        
        isFranchise_dt = ''
        if input['isFranchise'] == 'Franchise':
            isFranchise_dt = 'Franchise'
        else:
            isFranchise_dt = 'No Franchise'

        UrbanRural_dt = ''
        if input['UrbanRural'] == '1':
            UrbanRural_dt = 'Urban'
        else:
            UrbanRural_dt = 'Rural'
        
        sameState_dt = ''
        if input['sameState'] == '0':
            sameState_dt = 'Different State'
        else:
            sameState_dt = 'Same State'

        NAICS_dt = ''
        if input['sector'] == 'Ag_fores_ﬁshi_hunting':
            NAICS_dt = 'Agriculture, forestry, fishing and hunting'
        elif input['sector'] == 'Mining_quar_oil_gas_ext':
            NAICS_dt = 'Mining, quarrying, and oil and gas extraction'
        elif input['sector'] == 'Utilities':
            NAICS_dt = 'Utilities'
        elif input['sector'] == 'Construction':
            NAICS_dt = 'Construction'
        elif input['sector'] == 'Wholesale_trade':
            NAICS_dt = 'Wholesale trade'
        elif input['sector'] == 'Retail_trade':
            NAICS_dt = 'Retail trade'
        elif input['sector'] == 'Trans_&_Ware':
            NAICS_dt = 'Transportation and warehousing'
        elif input['sector'] == 'Information':
            NAICS_dt = 'Information'
        elif input['sector'] == 'Finance_insurance':
            NAICS_dt = 'Finance and insurance'
        elif input['sector'] == 'RE_rental_leasing':
            NAICS_dt = 'Real estate and rental and leasing'
        elif input['sector'] == 'Prof_scien_and_tech_serv':
            NAICS_dt = 'Professional, scientific, and technical services'
        elif input['sector'] == 'Management_and_enterprises':
            NAICS_dt = 'Management of companies and enterprises'
        elif input['sector'] == 'Admini_sup_and_waste_mgm_rem':
            NAICS_dt = 'Administrative and support and waste management and remediation services'
        elif input['sector'] == 'Educational services':
            NAICS_dt = 'Educational services'
        elif input['sector'] == 'Health_care_social_ass':
            NAICS_dt = 'Health care and social assistance'
        elif input['sector'] == 'Arts_enter_recreation':
            NAICS_dt = 'Arts, entertainment, and recreation'
        elif input['sector'] == 'Accommodation_food_serv':
            NAICS_dt = 'Accommodation and food services'
        elif input['sector'] == 'Other_no_pub':
            NAICS_dt = 'Other services (except public administration'
        elif input['sector'] == 'Public_admin':
            NAICS_dt = 'Public administration'
        elif input['sector'] == 'Manufacturing':
            NAICS_dt = 'Manufacturing'

        return render_template('result.html',
            Term=int(input['Term']),
            UrbanRural=UrbanRural_dt,
            isFranchise=isFranchise_dt,
            GrAppv = float(input['GrAppv']),
            sector=NAICS_dt,
            sameState=sameState_dt,
            NoEmp = int(input['NoEmp']),
            sba_pred = result
            )

if __name__ =='__main__':
    model = joblib.load('ModelSBA_RF_tuned_sm_sample')
    app.run(debug=True)

