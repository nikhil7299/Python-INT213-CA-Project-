from tkinter import*
from tkinter import font
from tkmacosx import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from typing import Collection
import mysql.connector



class VoterID:
    def __init__(self,root):
        self.root=root
        self.root.title("Villagers VoterID Data Management System")
        self.root.geometry("1680x1050+0+0")
        
        self.VoterID=StringVar()
        self.EName=StringVar()
        self.Gender=StringVar()
        self.HName=StringVar()
        self.FName=StringVar()
        self.DOB=StringVar()
        self.Pincode=StringVar()
        self.State=StringVar()
        self.District=StringVar()
        self.Area=StringVar()
        self.Town=StringVar()
        self.Anchal=StringVar()
        self.Date=StringVar() 
        

        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Villagers VoterID Data Management System",fg="teal",bg="white",font=("Times New Roman",45,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ==========DataFrame==========
        DataFrame=Frame(self.root,bd=10,relief=RIDGE)
        DataFrame.place(x=0,y=80,width=1680,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=5,relief=SOLID,padx=50,pady=50,
            font=("arial",12,"bold",UNDERLINE),text="VoterID Information")
        DataFrameLeft.place(x=8,y=5,width=1020,height=365)

        DataFrameRight=LabelFrame(DataFrame,bd=5,relief=SOLID,
            font=("arial",12,"bold",UNDERLINE),text="VoterID Details")
        DataFrameRight.place(x=1038,y=5,width=610,height=365)

        # ================Buttons Frame======================-
        Buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=490,width=1680,height=60)

        # ===================Details Frame====================
        Detailsframe=Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=550,width=1680,height=380)

        # ======================DataFrameLeft==================
        lblVoterID=Label(DataFrameLeft,text="VoterID: ",font=("arial",15,"bold"))
        lblVoterID.grid(row=0,column=0,sticky=W)
        txtVoterID=Entry(DataFrameLeft,textvariable=self.VoterID,font=("arial",15,"bold"),width=32)
        txtVoterID.grid(row=0,column=1)

        lblEName=Label(DataFrameLeft,text="Elector's Name: ",font=("arial",15,"bold"))
        lblEName.grid(row=1,column=0,sticky=W)
        txtEName=Entry(DataFrameLeft,textvariable=self.EName,font=("arial",15,"bold"),width=32)
        txtEName.grid(row=1,column=1)

        Gender=["Male","Female","Others"]
        lblGender=Label(DataFrameLeft, text="Gender: ",font=("arial",15,"bold")).grid(row=2,column=0, sticky=W)
        comGender=ttk.Combobox(DataFrameLeft,value=Gender,textvariable=self.Gender,state="readonly",font=("arial",15,"bold"),width=30 )
        # comState.current(0)
        comGender.grid(row=2,column=1)

        lblHName=Label(DataFrameLeft,text="Husband's Name: ",font=("arial",15,"bold"),)
        lblHName.grid(row=3,column=0,sticky=W)
        txtHName=Entry(DataFrameLeft,textvariable=self.HName,font=("arial",15,"bold"),width=32)
        
        # lblHNameInfo=Label(DataFrameLeft,text='( Leave "NIL" If Unmarried )',fg="grey",bg="white",font=("arial",15),padx=-30)
        # lblHNameInfo.grid(row=2,column=1)
        txtHName.insert(0,"NIL")
        txtHName.grid(row=3,column=1)

        lblFName=Label(DataFrameLeft,text="Father's Name: ",font=("arial",15,"bold"))
        lblFName.grid(row=4,column=0,sticky=W)
        txtFName=Entry(DataFrameLeft,textvariable=self.FName,font=("arial",15,"bold"),width=32)
        # txtFName.insert(0,"NIL")
        txtFName.grid(row=4,column=1)

        lblDOB=Label(DataFrameLeft,text="Date Of Birth: ",font=("arial",15,"bold"))
        lblDOB.grid(row=5,column=0,sticky=W)
        txtDOB=Entry(DataFrameLeft,textvariable=self.DOB,font=("arial",15,"bold"),width=32)
        txtDOB.grid(row=5,column=1)


        lblPincode=Label(DataFrameLeft,font=("arial",15,"bold"),text="Pincode: ")
        lblPincode.grid (row=6, column=0, sticky=W)
        txtPincode=Entry (DataFrameLeft,textvariable=self.Pincode ,font= ("arial", 15, "bold"), width=32)
        txtPincode.grid(row=6,column=1)

        lblState=Label (DataFrameLeft, font=("arial", 15, "bold"), text="State: ",padx=30)
        lblState.grid(row=0, column=2, sticky=W)
        
        States = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]

        AndhraPradesh = ["Achampet","Adilabad","Adoni","Alampur","Allagadda","Alur","Amalapuram","Amangallu","Anakapalle","Anantapur","Andole","Araku","Armoor","Asifabad","Aswaraopet","Atmakur","B. Kothakota","Badvel","Banaganapalle","Bandar","Bangarupalem","Banswada","Bapatla","Bellampalli","Bhadrachalam","Bhainsa","Bheemunipatnam","Bhimadole","Bhimavaram","Bhongir","Bhooragamphad","Boath","Bobbili","Bodhan","Chandoor","Chavitidibbalu","Chejerla","Chepurupalli","Cherial","Chevella","Chinnor","Chintalapudi","Chintapalle","Chirala","Chittoor","Chodavaram","Cuddapah","Cumbum","Darsi","Devarakonda","Dharmavaram","Dichpalli","Divi","Donakonda","Dronachalam","East Godavari","Eluru","Eturnagaram","Gadwal","Gajapathinagaram","Gajwel","Garladinne","Giddalur","Godavari","Gooty","Gudivada","Gudur","Guntur","Hindupur","Hunsabad","Huzurabad","Huzurnagar","Hyderabad","Ibrahimpatnam","Jaggayyapet","Jagtial","Jammalamadugu","Jangaon","Jangareddygudem","Jannaram","Kadiri","Kaikaluru","Kakinada","Kalwakurthy","Kalyandurg","Kamalapuram","Kamareddy","Kambadur","Kanaganapalle","Kandukuru","Kanigiri","Karimnagar","Kavali","Khammam","Khanapur (AP)","Kodangal","Koduru","Koilkuntla","Kollapur","Kothagudem","Kovvur","Krishna","Krosuru","Kuppam","Kurnool","Lakkireddipalli","Madakasira","Madanapalli","Madhira","Madnur","Mahabubabad","Mahabubnagar","Mahadevapur","Makthal","Mancherial","Mandapeta","Mangalagiri","Manthani","Markapur","Marturu","Medachal","Medak","Medarmetla","Metpalli","Mriyalguda","Mulug","Mylavaram","Nagarkurnool","Nalgonda","Nallacheruvu","Nampalle","Nandigama","Nandikotkur","Nandyal","Narasampet","Narasaraopet","Narayanakhed","Narayanpet","Narsapur","Narsipatnam","Nazvidu","Nelloe","Nellore","Nidamanur","Nirmal","Nizamabad","Nuguru","Ongole","Outsarangapalle","Paderu","Pakala","Palakonda","Paland","Palmaneru","Pamuru","Pargi","Parkal","Parvathipuram","Pathapatnam","Pattikonda","Peapalle","Peddapalli","Peddapuram","Penukonda","Piduguralla","Piler","Pithapuram","Podili","Polavaram","Prakasam","Proddatur","Pulivendla","Punganur","Putturu","Rajahmundri","Rajampeta","Ramachandrapuram","Ramannapet","Rampachodavaram","Rangareddy","Rapur","Rayachoti","Rayadurg","Razole","Repalle","Saluru","Sangareddy","Sathupalli","Sattenapalle","Satyavedu","Shadnagar","Siddavattam","Siddipet","Sileru","Sircilla","Sirpur Kagaznagar","Sodam","Sompeta","Srikakulam","Srikalahasthi","Srisailam","Srungavarapukota","Sudhimalla","Sullarpet","Tadepalligudem","Tadipatri","Tanduru","Tanuku","Tekkali","Tenali","Thungaturthy","Tirivuru","Tirupathi","Tuni","Udaygiri","Ulvapadu","Uravakonda","Utnor","V.R. Puram","Vaimpalli","Vayalpad","Venkatgiri","Venkatgirikota","Vijayawada","Vikrabad","Vinjamuru","Vinukonda","Visakhapatnam","Vizayanagaram","Vizianagaram","Vuyyuru","Wanaparthy","Warangal","Wardhannapet","Yelamanchili","Yelavaram","Yeleswaram","Yellandu","Yellanuru","Yellareddy","Yerragondapalem","Zahirabad "]


        ArunachalPradesh = ["Along","Anini","Anjaw","Bameng","Basar","Changlang","Chowkhem","Daporizo","Dibang Valley","Dirang","Hayuliang","Huri","Itanagar","Jairampur","Kalaktung","Kameng","Khonsa","Kolaring","Kurung Kumey","Lohit","Lower Dibang Valley","Lower Subansiri","Mariyang","Mechuka","Miao","Nefra","Pakkekesang","Pangin","Papum Pare","Passighat","Roing","Sagalee","Seppa","Siang","Tali","Taliha","Tawang","Tezu","Tirap","Tuting","Upper Siang","Upper Subansiri","Yiang Kiag "]


        Assam= ["Abhayapuri","Baithalangshu","Barama","Barpeta Road","Bihupuria","Bijni","Bilasipara","Bokajan","Bokakhat","Boko","Bongaigaon","Cachar","Cachar Hills","Darrang","Dhakuakhana","Dhemaji","Dhubri","Dibrugarh","Digboi","Diphu","Goalpara","Gohpur","Golaghat","Guwahati","Hailakandi","Hajo","Halflong","Hojai","Howraghat","Jorhat","Kamrup","Karbi Anglong","Karimganj","Kokarajhar","Kokrajhar","Lakhimpur","Maibong","Majuli","Mangaldoi","Mariani","Marigaon","Moranhat","Morigaon","Nagaon","Nalbari","Rangapara","Sadiya","Sibsagar","Silchar","Sivasagar","Sonitpur","Tarabarihat","Tezpur","Tinsukia","Udalgiri","Udalguri","UdarbondhBarpeta"]

        Bihar= ["Adhaura","Amarpur","Araria ","Areraj","Arrah","Arwal ","Aurangabad ","Bagaha ","Banka ","Banmankhi ","Barachakia ","Barauni ","Barh ","Barosi ","Begusarai ","Benipatti ","Benipur ","Bettiah ","Bhabhua ","Bhagalpur ","Bhojpur ","Bidupur ","Biharsharif ","Bikram ","Bikramganj ","Birpur ","Buxar ","Chakai ","Champaran ","Chapara ","Dalsinghsarai ","Danapur ","Darbhanga ","Daudnagar ","Dhaka ","Dhamdaha ","Dumraon ","Ekma ","Forbesganj ","Gaya ","Gogri ","Gopalganj ","H.Kharagpur ","Hajipur ","Hathua ","Hilsa ","Imamganj ","Jahanabad ","Jainagar ","Jamshedpur ","Jamui ","Jehanabad ","Jhajha ","Jhanjharpur ","Kahalgaon ","Kaimur (Bhabua) ","Katihar ","Katoria ","Khagaria ","Kishanganj ","Korha ","Lakhisarai ","Madhepura ","Madhubani ","Maharajganj ","Mahua ","Mairwa ","Mallehpur ","Masrakh ","Mohania ","Monghyr ","Motihari ","Motipur ","Munger ","Muzaffarpur ","Nabinagar ","Nalanda ","Narkatiaganj ","Naugachia ","Nawada ","Pakribarwan ","Pakridayal ","Patna ","Phulparas ","Piro ","Pupri ","Purena ","Purnia ","Rafiganj ","Rajauli ","Ramnagar ","Raniganj ","Raxaul ","Rohtas ","Rosera ","S.Bakhtiarpur ","Saharsa ","Samastipur ","Saran ","Sasaram ","Seikhpura ","Sheikhpura ","Sheohar ","Sherghati ","Sidhawalia ","Singhwara ","Sitamarhi ","Siwan ","Sonepur ","Supaul ","Thakurganj ","Triveniganj ","Udakishanganj ","Vaishali ","Wazirganj"]

        Chhattisgarh = ["Ambikapur","Antagarh","Arang","Bacheli","Bagbahera","Bagicha","Baikunthpur","Balod","Balodabazar","Balrampur","Barpalli","Basana","Bastanar","Bastar","Bderajpur","Bemetara","Berla","Bhairongarh","Bhanupratappur","Bharathpur","Bhatapara","Bhilai","Bhilaigarh","Bhopalpatnam","Bijapur","Bilaspur","Bodla","Bokaband","Chandipara","Chhinagarh","Chhuriakala","Chingmut","Chuikhadan","Dabhara","Dallirajhara","Dantewada","Deobhog","Dhamda","Dhamtari","Dharamjaigarh","Dongargarh","Durg","Durgakondal","Fingeshwar","Gariaband","Garpa","Gharghoda","Gogunda","Ilamidi","Jagdalpur","Janjgir","Janjgir-Champa","Jarwa","Jashpur","Jashpurnagar","Kabirdham-Kawardha","Kanker","Kasdol","Kathdol","Kathghora","Kawardha","Keskal","Khairgarh","Kondagaon","Konta","Korba","Korea","Kota","Koyelibeda","Kuakunda","Kunkuri","Kurud","Lohadigundah","Lormi","Luckwada","Mahasamund","Makodi","Manendragarh","Manpur","Marwahi","Mohla","Mungeli","Nagri","Narainpur","Narayanpur","Neora","Netanar","Odgi","Padamkot","Pakhanjur","Pali","Pandaria","Pandishankar","Parasgaon","Pasan","Patan","Pathalgaon","Pendra","Pratappur","Premnagar","Raigarh","Raipur","Rajnandgaon","Rajpur","Ramchandrapur","Saraipali","Saranggarh","Sarona","Semaria","Shakti","Sitapur","Sukma","Surajpur","Surguja","Tapkara","Toynar","Udaipur","Uproda","Wadrainagar"]

        Goa = ["Canacona","Candolim","Chinchinim","Cortalim","Goa","Jua","Madgaon","Mahem","Mapuca","Marmagao","Panji","Ponda","Sanvordem","Terekhol "]

        Gujarat = ["Ahmedabad","Ahwa","Amod","Amreli","Anand","Anjar","Ankaleshwar","Babra","Balasinor","Banaskantha","Bansada","Bardoli","Bareja","Baroda","Barwala","Bayad","Bhachav","Bhanvad","Bharuch","Bhavnagar","Bhiloda","Bhuj","Billimora","Borsad","Botad","Chanasma","Chhota Udaipur","Chotila","Dabhoi","Dahod","Damnagar","Dang","Danta","Dasada","Dediapada","Deesa","Dehgam","Deodar","Devgadhbaria","Dhandhuka","Dhanera","Dharampur","Dhari","Dholka","Dhoraji","Dhrangadhra","Dhrol","Dwarka","Fortsongadh","Gadhada","Gandhi Nagar","Gariadhar","Godhra","Gogodar","Gondal","Halol","Halvad","Harij","Himatnagar","Idar","Jambusar","Jamjodhpur","Jamkalyanpur","Jamnagar","Jasdan","Jetpur","Jhagadia","Jhalod","Jodia","Junagadh","Junagarh","Kalawad","Kalol","Kapad Wanj","Keshod","Khambat","Khambhalia","Khavda","Kheda","Khedbrahma","Kheralu","Kodinar","Kotdasanghani","Kunkawav","Kutch","Kutchmandvi","Kutiyana","Lakhpat","Lakhtar","Lalpur","Limbdi","Limkheda","Lunavada","M.M.Mangrol","Mahuva","Malia-Hatina","Maliya","Malpur","Manavadar","Mandvi","Mangrol","Mehmedabad","Mehsana","Miyagam","Modasa","Morvi","Muli","Mundra","Nadiad","Nakhatrana","Nalia","Narmada","Naswadi","Navasari","Nizar","Okha","Paddhari","Padra","Palanpur","Palitana","Panchmahals","Patan","Pavijetpur","Porbandar","Prantij","Radhanpur","Rahpar","Rajaula","Rajkot","Rajpipla","Ranavav","Sabarkantha","Sanand","Sankheda","Santalpur","Santrampur","Savarkundla","Savli","Sayan","Sayla","Shehra","Sidhpur","Sihor","Sojitra","Sumrasar","Surat","Surendranagar","Talaja","Thara","Tharad","Thasra","Una-Diu","Upleta","Vadgam","Vadodara","Valia","Vallabhipur","Valod","Valsad","Vanthali","Vapi","Vav","Veraval","Vijapur","Viramgam","Visavadar","Visnagar","Vyara","Waghodia","Wankaner "]

        Haryana = ["Adampur Mandi","Ambala","Assandh","Bahadurgarh","Barara","Barwala","Bawal","Bawanikhera","Bhiwani","Charkhidadri","Cheeka","Chhachrauli","Dabwali","Ellenabad","Faridabad","Fatehabad","Ferojpur Jhirka","Gharaunda","Gohana","Gurgaon","Hansi","Hisar","Jagadhari","Jatusana","Jhajjar","Jind","Julana","Kaithal","Kalanaur","Kalanwali","Kalka","Karnal","Kosli","Kurukshetra","Loharu","Mahendragarh","Meham","Mewat","Mohindergarh","Naraingarh","Narnaul","Narwana","Nilokheri","Nuh","Palwal","Panchkula","Panipat","Pehowa","Ratia","Rewari","Rohtak","Safidon","Sirsa","Siwani","Sonipat","Tohana","Tohsam","Yamunanagar "]

        HimachalPradesh = ["Amb","Arki","Banjar","Bharmour","Bilaspur","Chamba","Churah","Dalhousie","Dehra Gopipur","Hamirpur","Jogindernagar","Kalpa","Kangra","Kinnaur","Kullu","Lahaul","Mandi","Nahan","Nalagarh","Nirmand","Nurpur","Palampur","Pangi","Paonta","Pooh","Rajgarh","Rampur Bushahar","Rohru","Shimla","Sirmaur","Solan","Spiti","Sundernagar","Theog","Udaipur","Una"]

        JammuKashmir = ["Akhnoor","Anantnag","Badgam","Bandipur","Baramulla","Basholi","Bedarwah","Budgam","Doda","Gulmarg","Jammu","Kalakot","Kargil","Karnah","Kathua","Kishtwar","Kulgam","Kupwara","Leh","Mahore","Nagrota","Nobra","Nowshera","Nyoma","Padam","Pahalgam","Patnitop","Poonch","Pulwama","Rajouri","Ramban","Ramnagar","Reasi","Samba","Srinagar","Udhampur","Vaishno Devi "]

        Jharkhand =["Bagodar","Baharagora","Balumath","Barhi","Barkagaon","Barwadih","Basia","Bermo","Bhandaria","Bhawanathpur","Bishrampur","Bokaro","Bolwa","Bundu","Chaibasa","Chainpur","Chakardharpur","Chandil","Chatra","Chavparan","Daltonganj","Deoghar","Dhanbad","Dumka","Dumri","Garhwa","Garu","Ghaghra","Ghatsila","Giridih","Godda","Gomia","Govindpur","Gumla","Hazaribagh","Hunterganj","Ichak","Itki","Jagarnathpur","Jamshedpur","Jamtara","Japla","Jharmundi","Jhinkpani","Jhumaritalaiya","Kathikund","Kharsawa","Khunti","Koderma","Kolebira","Latehar","Lohardaga","Madhupur","Mahagama","Maheshpur Raj","Mandar","Mandu","Manoharpur","Muri","Nagarutatri","Nala","Noamundi","Pakur","Palamu","Palkot","Patan","Rajdhanwar","Rajmahal","Ramgarh","Ranchi","Sahibganj","Saraikela","Simaria","Simdega","Singhbhum","Tisri","Torpa "]

        Karnataka =["Afzalpur","Ainapur","Aland","Alur","Anekal","Ankola","Arsikere","Athani","Aurad","Bableshwar","Badami","Bagalkot","Bagepalli","Bailhongal","Bangalore","Bangalore Rural","Bangarpet","Bantwal","Basavakalyan","Basavanabagewadi","Basavapatna","Belgaum","Bellary","Belthangady","Belur","Bhadravati","Bhalki","Bhatkal","Bidar","Bijapur","Biligi","Chadchan","Challakere","Chamrajnagar","Channagiri","Channapatna","Channarayapatna","Chickmagalur","Chikballapur","Chikkaballapur","Chikkanayakanahalli","Chikkodi","Chikmagalur","Chincholi","Chintamani","Chitradurga","Chittapur","Cowdahalli","Davanagere","Deodurga","Devangere","Devarahippargi","Dharwad","Doddaballapur","Gadag","Gangavathi","Gokak","Gowribdanpur","Gubbi","Gulbarga","Gundlupet","H.B.Halli","H.D. Kote","Haliyal","Hampi","Hangal","Harapanahalli","Hassan","Haveri","Hebri","Hirekerur","Hiriyur","Holalkere","Holenarsipur","Honnali","Honnavar","Hosadurga","Hosakote","Hosanagara","Hospet","Hubli","Hukkeri","Humnabad","Hungund","Hunsagi","Hunsur","Huvinahadagali","Indi","Jagalur","Jamkhandi","Jewargi","Joida","K.R. Nagar","Kadur","Kalghatagi","Kamalapur","Kanakapura","Kannada","Kargal","Karkala","Karwar","Khanapur","Kodagu","Kolar","Kollegal","Koppa","Koppal","Koratageri","Krishnarajapet","Kudligi","Kumta","Kundapur","Kundgol","Kunigal","Kurugodu","Kustagi","Lingsugur","Madikeri","Madugiri","Malavalli","Malur","Mandya","Mangalore","Manipal","Manvi","Mashal","Molkalmuru","Mudalgi","Muddebihal","Mudhol","Mudigere","Mulbagal","Mundagod","Mundargi","Murugod","Mysore","Nagamangala","Nanjangud","Nargund","Narsimrajapur","Navalgund","Nelamangala","Nimburga","Pandavapura","Pavagada","Puttur","Raibag","Raichur","Ramdurg","Ranebennur","Ron","Sagar","Sakleshpur","Salkani","Sandur","Saundatti","Savanur","Sedam","Shahapur","Shankarnarayana","Shikaripura","Shimoga","Shirahatti","Shorapur","Siddapur","Sidlaghatta","Sindagi","Sindhanur","Sira","Sirsi","Siruguppa","Somwarpet","Sorab","Sringeri","Sriniwaspur","Srirangapatna","Sullia","T. Narsipur","Tallak","Tarikere","Telgi","Thirthahalli","Tiptur","Tumkur","Turuvekere","Udupi","Virajpet","Wadi","Yadgiri","Yelburga","Yellapur "]

        Kerala=["Adimaly","Adoor","Agathy","Alappuzha","Alathur","Alleppey","Alwaye","Amini","Androth","Attingal","Badagara","Bitra","Calicut","Cannanore","Chetlet","Ernakulam","Idukki","Irinjalakuda","Kadamath","Kalpeni","Kalpetta","Kanhangad","Kanjirapally","Kannur","Karungapally","Kasargode","Kavarathy","Kiltan","Kochi","Koduvayur","Kollam","Kottayam","Kovalam","Kozhikode","Kunnamkulam","Malappuram","Mananthodi","Manjeri","Mannarghat","Mavelikkara","Minicoy","Munnar","Muvattupuzha","Nedumandad","Nedumgandam","Nilambur","Palai","Palakkad","Palghat","Pathaanamthitta","Pathanamthitta","Payyanur","Peermedu","Perinthalmanna","Perumbavoor","Punalur","Quilon","Ranni","Shertallai","Shoranur","Taliparamba","Tellicherry","Thiruvananthapuram","Thodupuzha","Thrissur","Tirur","Tiruvalla","Trichur","Trivandrum","Uppala","Vadakkanchery","Vikom","Wayanad "]

        MadhyaPradesh=["Agar","Ajaigarh","Alirajpur","Amarpatan","Amarwada","Ambah","Anuppur","Arone","Ashoknagar","Ashta","Atner","Babaichichli","Badamalhera","Badarwsas","Badnagar","Badnawar","Badwani","Bagli","Baihar","Balaghat","Baldeogarh","Baldi","Bamori","Banda","Bandhavgarh","Bareli","Baroda","Barwaha","Barwani","Batkakhapa","Begamganj","Beohari","Berasia","Berchha","Betul","Bhainsdehi","Bhander","Bhanpura","Bhikangaon","Bhimpur","Bhind","Bhitarwar","Bhopal","Biaora","Bijadandi","Bijawar","Bijaypur","Bina","Birsa","Birsinghpur","Budhni","Burhanpur","Buxwaha","Chachaura","Chanderi","Chaurai","Chhapara","Chhatarpur","Chhindwara","Chicholi","Chitrangi","Churhat","Dabra","Damoh","Datia","Deori","Deosar","Depalpur","Dewas","Dhar","Dharampuri","Dindori","Gadarwara","Gairatganj","Ganjbasoda","Garoth","Ghansour","Ghatia","Ghatigaon","Ghorandogri","Ghughari","Gogaon","Gohad","Goharganj","Gopalganj","Gotegaon","Gourihar","Guna","Gunnore","Gwalior","Gyraspur","Hanumana","Harda","Harrai","Harsud","Hatta","Hoshangabad","Ichhawar","Indore","Isagarh","Itarsi","Jabalpur","Jabera","Jagdalpur","Jaisinghnagar","Jaithari","Jaitpur","Jaitwara","Jamai","Jaora","Jatara","Jawad","Jhabua","Jobat","Jora","Kakaiya","Kannod","Kannodi","Karanjia","Kareli","Karera","Karhal","Karpa","Kasrawad","Katangi","Katni","Keolari","Khachrod","Khajuraho","Khakner","Khalwa","Khandwa","Khaniadhana","Khargone","Khategaon","Khetia","Khilchipur","Khirkiya","Khurai","Kolaras","Kotma","Kukshi","Kundam","Kurwai","Kusmi","Laher","Lakhnadon","Lamta","Lanji","Lateri","Laundi","Maheshwar","Mahidpurcity","Maihar","Majhagwan","Majholi","Malhargarh","Manasa","Manawar","Mandla","Mandsaur","Manpur","Mauganj","Mawai","Mehgaon","Mhow","Morena","Multai","Mungaoli","Nagod","Nainpur","Narsingarh","Narsinghpur","Narwar","Nasrullaganj","Nateran","Neemuch","Niwari","Niwas","Nowgaon","Pachmarhi","Pandhana","Pandhurna","Panna","Parasia","Patan","Patera","Patharia","Pawai","Petlawad","Pichhore","Piparia","Pohari","Prabhapattan","Punasa","Pushprajgarh","Raghogarh","Raghunathpur","Rahatgarh","Raisen","Rajgarh","Rajpur","Ratlam","Rehli","Rewa","Sabalgarh","Sagar","Sailana","Sanwer","Sarangpur","Sardarpur","Satna","Saunsar","Sehore","Sendhwa","Seondha","Seoni","Seonimalwa","Shahdol","Shahnagar","Shahpur","Shajapur","Sheopur","Sheopurkalan","Shivpuri","Shujalpur","Sidhi","Sihora","Silwani","Singrauli","Sirmour","Sironj","Sitamau","Sohagpur","Sondhwa","Sonkatch","Susner","Tamia","Tarana","Tendukheda","Teonthar","Thandla","Tikamgarh","Timarani","Udaipura","Ujjain","Umaria","Umariapan","Vidisha","Vijayraghogarh","Waraseoni","Zhirnia "]

        Maharashtra=["Achalpur","Aheri","Ahmednagar","Ahmedpur","Ajara","Akkalkot","Akola","Akole","Akot","Alibagh","Amagaon","Amalner","Ambad","Ambejogai","Amravati","Arjuni Merogaon","Arvi","Ashti","Atpadi","Aurangabad","Ausa","Babhulgaon","Balapur","Baramati","Barshi Takli","Barsi","Basmatnagar","Bassein","Beed","Bhadrawati","Bhamregadh","Bhandara","Bhir","Bhiwandi","Bhiwapur","Bhokar","Bhokardan","Bhoom","Bhor","Bhudargad","Bhusawal","Billoli","Brahmapuri","Buldhana","Butibori","Chalisgaon","Chamorshi","Chandgad","Chandrapur","Chandur","Chanwad","Chhikaldara","Chikhali","Chinchwad","Chiplun","Chopda","Chumur","Dahanu","Dapoli","Darwaha","Daryapur","Daund","Degloor","Delhi Tanda","Deogad","Deolgaonraja","Deori","Desaiganj","Dhadgaon","Dhanora","Dharani","Dhiwadi","Dhule","Dhulia","Digras","Dindori","Edalabad","Erandul","Etapalli","Gadhchiroli","Gadhinglaj","Gaganbavada","Gangakhed","Gangapur","Gevrai","Ghatanji","Golegaon","Gondia","Gondpipri","Goregaon","Guhagar","Hadgaon","Hatkangale","Hinganghat","Hingoli","Hingua","Igatpuri","Indapur","Islampur","Jalgaon","Jalna","Jamkhed","Jamner","Jath","Jawahar","Jintdor","Junnar","Kagal","Kaij","Kalamb","Kalamnuri","Kallam","Kalmeshwar","Kalwan","Kalyan","Kamptee","Kandhar","Kankavali","Kannad","Karad","Karjat","Karmala","Katol","Kavathemankal","Kedgaon","Khadakwasala","Khamgaon","Khed","Khopoli","Khultabad","Kinwat","Kolhapur","Kopargaon","Koregaon","Kudal","Kuhi","Kurkheda","Kusumba","Lakhandur","Langa","Latur","Lonar","Lonavala","Madangad","Madha","Mahabaleshwar","Mahad","Mahagaon","Mahasala","Mahaswad","Malegaon","Malgaon","Malgund","Malkapur","Malsuras","Malwan","Mancher","Mangalwedha","Mangaon","Mangrulpur","Manjalegaon","Manmad","Maregaon","Mehda","Mekhar","Mohadi","Mohol","Mokhada","Morshi","Mouda","Mukhed","Mul","Mumbai","Murbad","Murtizapur","Murud","Nagbhir","Nagpur","Nahavara","Nanded","Nandgaon","Nandnva","Nandurbar","Narkhed","Nashik","Navapur","Ner","Newasa","Nilanga","Niphad","Omerga","Osmanabad","Pachora","Paithan","Palghar","Pali","Pandharkawada","Pandharpur","Panhala","Paranda","Parbhani","Parner","Parola","Parseoni","Partur","Patan","Pathardi","Pathari","Patoda","Pauni","Peint","Pen","Phaltan","Pimpalner","Pirangut","Poladpur","Pune","Pusad","Pusegaon","Radhanagar","Rahuri","Raigad","Rajapur","Rajgurunagar","Rajura","Ralegaon","Ramtek","Ratnagiri","Raver","Risod","Roha","Sakarwadi","Sakoli","Sakri","Salekasa","Samudrapur","Sangamner","Sanganeshwar","Sangli","Sangola","Sanguem","Saoner","Saswad","Satana","Satara","Sawantwadi","Seloo","Shahada","Shahapur","Shahuwadi","Shevgaon","Shirala","Shirol","Shirpur","Shirur","Shirwal","Sholapur","Shri Rampur","Shrigonda","Shrivardhan","Sillod","Sinderwahi","Sindhudurg","Sindkheda","Sindkhedaraja","Sinnar","Sironcha","Soyegaon","Surgena","Talasari","Talegaon S.Ji Pant","Taloda","Tasgaon","Thane","Tirora","Tiwasa","Trimbak","Tuljapur","Tumsar","Udgir","Umarkhed","Umrane","Umrer","Urlikanchan","Vaduj","Velhe","Vengurla","Vijapur","Vita","Wada","Wai","Walchandnagar","Wani","Wardha","Warlydwarud","Warora","Washim","Wathar","Yavatmal","Yawal","Yeola","Yeotmal "]

        Manipur=["Bishnupur","Chakpikarong","Chandel","Chattrik","Churachandpur","Imphal","Jiribam","Kakching","Kalapahar","Mao","Mulam","Parbung","Sadarhills","Saibom","Sempang","Senapati","Sochumer","Taloulong","Tamenglong","Thinghat","Thoubal","Ukhrul "]

        Meghalaya=["Amlaren","Baghmara","Cherrapunjee","Dadengiri","Garo Hills","Jaintia Hills","Jowai","Khasi Hills","Khliehriat","Mariang","Mawkyrwat","Nongpoh","Nongstoin","Resubelpara","Ri Bhoi","Shillong","Tura","Williamnagar"]

        Mizoram=["Aizawl","Champhai","Demagiri","Kolasib","Lawngtlai","Lunglei","Mamit","Saiha","Serchhip"]

        Nagaland=["Dimapur","Jalukie","Kiphire","Kohima","Mokokchung","Mon","Phek","Tuensang","Wokha","Zunheboto"]

        Orissa=["Anandapur","Angul","Anugul","Aska","Athgarh","Athmallik","Attabira","Bagdihi","Balangir","Balasore","Baleswar","Baliguda","Balugaon","Banaigarh","Bangiriposi","Barbil","Bargarh","Baripada","Barkot","Basta","Berhampur","Betanati","Bhadrak","Bhanjanagar","Bhawanipatna","Bhubaneswar","Birmaharajpur","Bisam Cuttack","Boriguma","Boudh","Buguda","Chandbali","Chhatrapur","Chhendipada","Cuttack","Daringbadi","Daspalla","Deodgarh","Deogarh","Dhanmandal","Dharamgarh","Dhenkanal","Digapahandi","Dunguripali","G. Udayagiri","Gajapati","Ganjam","Ghatgaon","Gudari","Gunupur","Hemgiri","Hindol","Jagatsinghapur","Jajpur","Jamankira","Jashipur","Jayapatna","Jeypur","Jharigan","Jharsuguda","Jujumura","Kalahandi","Kalimela","Kamakhyanagar","Kandhamal","Kantabhanji","Kantamal","Karanjia","Kashipur","Kendrapara","Kendujhar","Keonjhar","Khalikote","Khordha","Khurda","Komana","Koraput","Kotagarh","Kuchinda","Lahunipara","Laxmipur","M. Rampur","Malkangiri","Mathili","Mayurbhanj","Mohana","Motu","Nabarangapur","Naktideul","Nandapur","Narlaroad","Narsinghpur","Nayagarh","Nimapara","Nowparatan","Nowrangapur","Nuapada","Padampur","Paikamal","Palla Hara","Papadhandi","Parajang","Pardip","Parlakhemundi","Patnagarh","Pattamundai","Phiringia","Phulbani","Puri","Puruna Katak","R. Udayigiri","Rairakhol","Rairangpur","Rajgangpur","Rajkhariar","Rayagada","Rourkela","Sambalpur","Sohela","Sonapur","Soro","Subarnapur","Sunabeda","Sundergarh","Surada","T. Rampur","Talcher","Telkoi","Titlagarh","Tumudibandha","Udala","Umerkote "]

        Punjab=["Abohar","Ajnala","Amritsar","Balachaur","Barnala","Batala","Bathinda","Chandigarh","Dasua","Dinanagar","Faridkot","Fatehgarh Sahib","Fazilka","Ferozepur","Garhashanker","Goindwal","Gurdaspur","Guruharsahai","Hoshiarpur","Jagraon","Jalandhar","Jugial","Kapurthala","Kharar","Kotkapura","Ludhiana","Malaut","Malerkotla","Mansa","Moga","Muktasar","Nabha","Nakodar","Nangal","Nawanshahar","Nawanshahr","Pathankot","Patiala","Patti","Phagwara","Phillaur","Phulmandi","Quadian","Rajpura","Raman","Rayya","Ropar","Rupnagar","Samana","Samrala","Sangrur","Sardulgarh","Sarhind","SAS Nagar","Sultanpur Lodhi","Sunam","Tanda Urmar","Tarn Taran","Zira "]

        Rajasthan=["Abu Road","Ahore","Ajmer","Aklera","Alwar","Amber","Amet","Anupgarh","Asind","Aspur","Atru","Bagidora","Bali","Bamanwas","Banera","Bansur","Banswara","Baran","Bari","Barisadri","Barmer","Baseri","Bassi","Baswa","Bayana","Beawar","Begun","Behror","Bhadra","Bharatpur","Bhilwara","Bhim","Bhinmal","Bikaner","Bilara","Bundi","Chhabra","Chhipaborad","Chirawa","Chittorgarh","Chohtan","Churu","Dantaramgarh","Dausa","Deedwana","Deeg","Degana","Deogarh","Deoli","Desuri","Dhariawad","Dholpur","Digod","Dudu","Dungarpur","Dungla","Fatehpur","Gangapur","Gangdhar","Gerhi","Ghatol","Girwa","Gogunda","Hanumangarh","Hindaun","Hindoli","Hurda","Jahazpur","Jaipur","Jaisalmer","Jalore","Jhalawar","Jhunjhunu","Jodhpur","Kaman","Kapasan","Karauli","Kekri","Keshoraipatan","Khandar","Kherwara","Khetri","Kishanganj","Kishangarh","Kishangarhbas","Kolayat","Kota","Kotputli","Kotra","Kotri","Kumbalgarh","Kushalgarh","Ladnun","Ladpura","Lalsot","Laxmangarh","Lunkaransar","Mahuwa","Malpura","Malvi","Mandal","Mandalgarh","Mandawar","Mangrol","Marwar-Jn","Merta","Nadbai","Nagaur","Nainwa","Nasirabad","Nathdwara","Nawa","Neem Ka Thana","Newai","Nimbahera","Nohar","Nokha","Onli","Osian","Pachpadara","Pachpahar","Padampur","Pali","Parbatsar","Phagi","Phalodi","Pilani","Pindwara","Pipalda","Pirawa","Pokaran","Pratapgarh","Raipur","Raisinghnagar","Rajgarh","Rajsamand","Ramganj Mandi","Ramgarh","Rashmi","Ratangarh","Reodar","Rupbas","Sadulshahar","Sagwara","Sahabad","Salumber","Sanchore","Sangaria","Sangod","Sapotra","Sarada","Sardarshahar","Sarwar","Sawai Madhopur","Shahapura","Sheo","Sheoganj","Shergarh","Sikar","Sirohi","Siwana","Sojat","Sri Dungargarh","Sri Ganganagar","Sri Karanpur","Sri Madhopur","Sujangarh","Taranagar","Thanaghazi","Tibbi","Tijara","Todaraisingh","Tonk","Udaipur","Udaipurwati","Uniayara","Vallabhnagar","Viratnagar"]

        Sikkim=["Barmiak","Be","Bhurtuk","Chhubakha","Chidam","Chubha","Chumikteng","Dentam","Dikchu","Dzongri","Gangtok","Gauzing","Gyalshing","Hema","Kerung","Lachen","Lachung","Lema","Lingtam","Lungthu","Mangan","Namchi","Namthang","Nanga","Nantang","Naya Bazar","Padamachen","Pakhyong","Pemayangtse","Phensang","Rangli","Rinchingpong","Sakyong","Samdong","Singtam","Siniolchu","Sombari","Soreng","Sosing","Tekhug","Temi","Tsetang","Tsomgo","Tumlong","Yangang","Yumtang "]

        TamilNadu=["Ambasamudram","Anamali","Arakandanallur","Arantangi","Aravakurichi","Ariyalur","Arkonam","Arni","Aruppukottai","Attur","Avanashi","Batlagundu","Bhavani","Chengalpattu","Chengam","Chennai","Chidambaram","Chingleput","Coimbatore","Courtallam","Cuddalore","Cumbum","Denkanikoitah","Devakottai","Dharampuram","Dharmapuri","Dindigul","Erode","Gingee","Gobichettipalayam","Gudalur","Gudiyatham","Harur","Hosur","Jayamkondan","Kallkurichi","Kanchipuram","Kangayam","Kanyakumari","Karaikal","Karaikudi","Karur","Keeranur","Kodaikanal","Kodumudi","Kotagiri","Kovilpatti","Krishnagiri","Kulithalai","Kumbakonam","Kuzhithurai","Madurai","Madurantgam","Manamadurai","Manaparai","Mannargudi","Mayiladuthurai","Mayiladutjurai","Mettupalayam","Metturdam","Mudukulathur","Mulanur","Musiri","Nagapattinam","Nagarcoil","Namakkal","Nanguneri","Natham","Neyveli","Nilgiris","Oddanchatram","Omalpur","Ootacamund","Ooty","Orathanad","Palacode","Palani","Palladum","Papanasam","Paramakudi","Pattukottai","Perambalur","Perundurai","Pollachi","Polur","Pondicherry","Ponnamaravathi","Ponneri","Pudukkottai","Rajapalayam","Ramanathapuram","Rameshwaram","Ranipet","Rasipuram","Salem","Sankagiri","Sankaran","Sathiyamangalam","Sivaganga","Sivakasi","Sriperumpudur","Srivaikundam","Tenkasi","Thanjavur","Theni","Thirumanglam","Thiruraipoondi","Thoothukudi","Thuraiyure","Tindivanam","Tiruchendur","Tiruchengode","Tiruchirappalli","Tirunelvelli","Tirupathur","Tirupur","Tiruttani","Tiruvallur","Tiruvannamalai","Tiruvarur","Tiruvellore","Tiruvettipuram","Trichy","Tuticorin","Udumalpet","Ulundurpet","Usiliampatti","Uthangarai","Valapady","Valliyoor","Vaniyambadi","Vedasandur","Vellore","Velur","Vilathikulam","Villupuram","Virudhachalam","Virudhunagar","Wandiwash","Yercaud "]

        Telangana = ["Adilabad","Bhadradri Kothagudem","Hyderabad","Jagtial","Jangaon","Jayashankar","Jogulamba","Kamareddy","Karimnagar","Khammam","Komaram Bheem","Mahabubabad","Mahbubnagar","Mancherial","Medak","Medchal","Nagarkurnool","Nalgonda","Nirmal","Nizamabad","Peddapalli","Rajanna Sircilla","Ranga Reddy","Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy","Warangal Rural","Warangal Urban","Yadadri Bhuvanagiri"]

        Tripura = ["Dhalai","Gomati","Khowai","North Tripura","Sepahijala","South Tripura","Unakoti","West Tripura"]

        UttarPradesh=["Achhnera","Agra","Akbarpur","Aliganj","Aligarh","Allahabad","Ambedkar Nagar","Amethi","Amiliya","Amroha","Anola","Atrauli","Auraiya","Azamgarh","Baberu","Badaun","Baghpat","Bagpat","Baheri","Bahraich","Ballia","Balrampur","Banda","Bansdeeh","Bansgaon","Bansi","Barabanki","Bareilly","Basti","Bhadohi","Bharthana","Bharwari","Bhogaon","Bhognipur","Bidhuna","Bijnore","Bikapur","Bilari","Bilgram","Bilhaur","Bindki","Bisalpur","Bisauli","Biswan","Budaun","Budhana","Bulandshahar","Bulandshahr","Capianganj","Chakia","Chandauli","Charkhari","Chhata","Chhibramau","Chirgaon","Chitrakoot","Chunur","Dadri","Dalmau","Dataganj","Debai","Deoband","Deoria","Derapur","Dhampur","Domariyaganj","Dudhi","Etah","Etawah","Faizabad","Farrukhabad","Fatehpur","Firozabad","Garauth","Garhmukteshwar","Gautam Buddha Nagar","Ghatampur","Ghaziabad","Ghazipur","Ghosi","Gonda","Gorakhpur","Gunnaur","Haidergarh","Hamirpur","Hapur","Hardoi","Harraiya","Hasanganj","Hasanpur","Hathras","Jalalabad","Jalaun","Jalesar","Jansath","Jarar","Jasrana","Jaunpur","Jhansi","Jyotiba Phule Nagar","Kadipur","Kaimganj","Kairana","Kaisarganj","Kalpi","Kannauj","Kanpur","Karchhana","Karhal","Karvi","Kasganj","Kaushambi","Kerakat","Khaga","Khair","Khalilabad","Kheri","Konch","Kumaon","Kunda","Kushinagar","Lalganj","Lalitpur","Lucknow","Machlishahar","Maharajganj","Mahoba","Mainpuri","Malihabad","Mariyahu","Math","Mathura","Mau","Maudaha","Maunathbhanjan","Mauranipur","Mawana","Meerut","Mehraun","Meja","Mirzapur","Misrikh","Modinagar","Mohamdabad","Mohamdi","Moradabad","Musafirkhana","Muzaffarnagar","Nagina","Najibabad","Nakur","Nanpara","Naraini","Naugarh","Nawabganj","Nighasan","Noida","Orai","Padrauna","Pahasu","Patti","Pharenda","Phoolpur","Phulpur","Pilibhit","Pitamberpur","Powayan","Pratapgarh","Puranpur","Purwa","Raibareli","Rampur","Ramsanehi Ghat","Rasara","Rath","Robertsganj","Sadabad","Safipur","Sagri","Saharanpur","Sahaswan","Sahjahanpur","Saidpur","Salempur","Salon","Sambhal","Sandila","Sant Kabir Nagar","Sant Ravidas Nagar","Sardhana","Shahabad","Shahganj","Shahjahanpur","Shikohabad","Shravasti","Siddharthnagar","Sidhauli","Sikandra Rao","Sikandrabad","Sitapur","Siyana","Sonbhadra","Soraon","Sultanpur","Tanda","Tarabganj","Tilhar","Unnao","Utraula","Varanasi","Zamania "]

        Uttarakhand=["Almora","Bageshwar","Bhatwari","Chakrata","Chamoli","Champawat","Dehradun","Deoprayag","Dharchula","Dunda","Haldwani","Haridwar","Joshimath","Karan Prayag","Kashipur","Khatima","Kichha","Lansdown","Munsiari","Mussoorie","Nainital","Pantnagar","Partapnagar","Pauri Garhwal","Pithoragarh","Purola","Rajgarh","Ranikhet","Roorkee","Rudraprayag","Tehri Garhwal","Udham Singh Nagar","Ukhimath","Uttarkashi "]

        WestBengal=["Adra","Alipurduar","Amlagora","Arambagh","Asansol","Balurghat","Bankura","Bardhaman","Basirhat","Berhampur","Bethuadahari","Birbhum","Birpara","Bishanpur","Bolpur","Bongoan","Bulbulchandi","Burdwan","Calcutta","Canning","Champadanga","Contai","Cooch Behar","Daimond Harbour","Dalkhola","Dantan","Darjeeling","Dhaniakhali","Dhuliyan","Dinajpur","Dinhata","Durgapur","Gangajalghati","Gangarampur","Ghatal","Guskara","Habra","Haldia","Harirampur","Harishchandrapur","Hooghly","Howrah","Islampur","Jagatballavpur","Jalpaiguri","Jhalda","Jhargram","Kakdwip","Kalchini","Kalimpong","Kalna","Kandi","Karimpur","Katwa","Kharagpur","Khatra","Krishnanagar","Mal Bazar","Malda","Manbazar","Mathabhanga","Medinipur","Mekhliganj","Mirzapur","Murshidabad","Nadia","Nagarakata","Nalhati","Nayagarh","Parganas","Purulia","Raiganj","Rampur Hat","Ranaghat","Seharabazar","Siliguri","Suri","Takipur","Tamluk"]

        AndamanNicobar=["Alipur","Andaman Island","Anderson Island","Arainj-Laka-Punga","Austinabad","Bamboo Flat","Barren Island","Beadonabad","Betapur","Bindraban","Bonington","Brookesabad","Cadell Point","Calicut","Chetamale","Cinque Islands","Defence Island","Digilpur","Dolyganj","Flat Island","Geinyale","Great Coco Island","Haddo","Havelock Island","Henry Lawrence Island","Herbertabad","Hobdaypur","Ilichar","Ingoie","Inteview Island","Jangli Ghat","Jhon Lawrence Island","Karen","Kartara","KYD Islannd","Landfall Island","Little Andmand","Little Coco Island","Long Island","Maimyo","Malappuram","Manglutan","Manpur","Mitha Khari","Neill Island","Nicobar Island","North Brother Island","North Passage Island","North Sentinel Island","Nothen Reef Island","Outram Island","Pahlagaon","Palalankwe","Passage Island","Phaiapong","Phoenix Island","Port Blair","Preparis Island","Protheroepur","Rangachang","Rongat","Rutland Island","Sabari","Saddle Peak","Shadipur","Smith Island","Sound Island","South Sentinel Island","Spike Island","Tarmugli Island","Taylerabad","Titaije","Toibalawe","Tusonabad","West Island","Wimberleyganj","Yadita"]

        Chandigarh=[" Chandigarh","Mani Marja"]

        DadraNagarHaveli=["Amal","Amli","Bedpa","Chikhli","Dadra & Nagar Haveli","Dahikhed","Dolara","Galonda","Kanadi","Karchond","Khadoli","Kharadpada","Kherabari","Kherdi","Kothar","Luari","Mashat","Rakholi","Rudana","Saili","Sili","Silvassa","Sindavni","Udva","Umbarkoi","Vansda","Vasona","Velugam"]

        DamanDiu=["Brancavare","Dagasi","Daman","Diu","Magarvara","Nagwa","Pariali","Passo Covo"]

        Lakshadweep=["Agatti Island","Bingaram Island","Bitra Island","Chetlat Island","Kadmat Island","Kalpeni Island","Kavaratti Island","Kiltan Island","Lakshadweep Sea","Minicoy Island","North Island","South Island"]

        Delhi=["Central Delhi","East Delhi","New Delhi","North Delhi","North East Delhi","North West Delhi","South Delhi","South West Delhi","West Delhi"]

        Puducherry=["Bahur","Karaikal","Mahe","Pondicherry","Purnankuppam","Valudavur","Villianur","Yanam"]
        



        comState=ttk.Combobox(DataFrameLeft,value=States,textvariable=self.State,state="readonly",font=("arial",15,"bold"),width=30 )
        # comState.current(0)
        comState.grid(row=0,column=3)


        def pickDistrict(e):
            if comState.get()=="Andhra Pradesh":
                comDistrict.config(values=AndhraPradesh)
                comDistrict.current(0)
            if comState.get()=="Arunachal Pradesh":
                comDistrict.config(values=ArunachalPradesh)
                comDistrict.current(0)
            if comState.get()=="Assam":
                comDistrict.config(values=Assam)
                comDistrict.current(0)
            if comState.get()=="Bihar":
                comDistrict.config(values=Bihar)
                comDistrict.current(0)
            if comState.get()=="Chhattisgarh":
                comDistrict.config(values=Chhattisgarh)
                comDistrict.current(0)
            if comState.get()=="Goa":
                comDistrict.config(values=Goa)
                comDistrict.current(0)
            if comState.get()=="Gujarat":
                comDistrict.config(values=Gujarat)
                comDistrict.current(0)
            if comState.get()=="Haryana":
                comDistrict.config(values=Haryana)
                comDistrict.current(0)
            if comState.get()=="Himachal Pradesh":
                comDistrict.config(values=HimachalPradesh)
                comDistrict.current(0)
            if comState.get()=="Jammu and Kashmir":
                comDistrict.config(values=JammuKashmir)
                comDistrict.current(0)
            if comState.get()=="Jharkhand":
                comDistrict.config(values=Jharkhand)
                comDistrict.current(0)
            if comState.get()=="Karnataka":
                comDistrict.config(values=Karnataka)
                comDistrict.current(0)
            if comState.get()=="Kerala":
                comDistrict.config(values=Kerala)
                comDistrict.current(0)
            if comState.get()=="Madhya Pradesh":
                comDistrict.config(values=MadhyaPradesh)
                comDistrict.current(0)
            if comState.get()=="Maharashtra":
                comDistrict.config(values=Maharashtra)
                comDistrict.current(0)
            if comState.get()=="Manipur":
                comDistrict.config(values=Manipur)
                comDistrict.current(0)
            if comState.get()=="Meghalaya":
                comDistrict.config(values=Meghalaya)
                comDistrict.current(0)
            if comState.get()=="Mizoram":
                comDistrict.config(values=Mizoram)
                comDistrict.current(0)
            if comState.get()=="Nagaland":
                comDistrict.config(values=Nagaland)
                comDistrict.current(0)
            if comState.get()=="Orissa":
                comDistrict.config(values=Orissa)
                comDistrict.current(0)
            if comState.get()=="Punjab":
                comDistrict.config(values=Punjab)
                comDistrict.current(0)
            if comState.get()=="Rajasthan":
                comDistrict.config(values=Rajasthan)
                comDistrict.current(0)
            if comState.get()=="Sikkim":
                comDistrict.config(values=Sikkim)
                comDistrict.current(0)
            if comState.get()=="Tamil Nadu":
                comDistrict.config(values=TamilNadu)
                comDistrict.current(0)
            if comState.get()=="Telangana":
                comDistrict.config(values=Telangana)
                comDistrict.current(0)
            if comState.get()=="Tripura":
                comDistrict.config(values=Tripura)
                comDistrict.current(0)
            if comState.get()=="Uttar Pradesh":
                comDistrict.config(values=UttarPradesh)
                comDistrict.current(0)
            if comState.get()=="Uttarakhand":
                comDistrict.config(values=Uttarakhand)
                comDistrict.current(0)
            if comState.get()=="West Bengal":
                comDistrict.config(values=WestBengal)
                comDistrict.current(0)
            if comState.get()=="Andaman and Nicobar Islands":
                comDistrict.config(values=AndamanNicobar)
                comDistrict.current(0)
            if comState.get()=="Chandigarh":
                comDistrict.config(values=Chandigarh)
                comDistrict.current(0)
            if comState.get()=="Dadra and Nagar Haveli":
                comDistrict.config(values=DadraNagarHaveli)
                comDistrict.current(0)
            if comState.get()=="Daman and Diu":
                comDistrict.config(values=DamanDiu)
                comDistrict.current(0)
            if comState.get()=="Lakshadweep":
                comDistrict.config(values=Lakshadweep)
                comDistrict.current(0)
            if comState.get()=="Delhi":
                comDistrict.config(values=Delhi)
                comDistrict.current(0)
            if comState.get()=="Puducherry":
                comDistrict.config(values=Puducherry)
                comDistrict.current(0)
            

        comState.bind("<<ComboboxSelected>>",pickDistrict)

        comDistrict=ttk.Combobox(DataFrameLeft,value=[" "],textvariable=self.District,state="readonly",font=("arial",15,"bold"),width=30 )
        comDistrict.current(0)
        comDistrict.grid(row=1,column=3)

        # txtState=Entry (DataFrameLeft, font= ("arial",15, "bold"), width=32)
        # txtState.grid (row=5, column=1)

        lblDistrict=Label (DataFrameLeft, font= ("arial", 15, "bold"), text="District: ", padx=30,pady=10)
        lblDistrict.grid(row=1, column=2, sticky=W)
        # txtDistrict=Entry (DataFrameLeft, font=("arial", 15, "bold") , width=32)
        # txtDistrict.grid (row=0, column=3)
                

        lblArea=Label (DataFrameLeft, font= ("arial",15, "bold"), text="Area/ Colony:",padx=30,pady=10)
        lblArea.grid(row=2, column=2, sticky=W)
        txtArea=Entry (DataFrameLeft,textvariable=self.Area, font= ("arial",15, "bold"), width=32)
        txtArea.grid (row=2, column=3)

        lblTown=Label (DataFrameLeft, font=("arial",15, "bold"), text="Town/ Village:", padx=30,pady=10)
        lblTown.grid(row=3, column=2, sticky=W)
        txtTown=Entry (DataFrameLeft,textvariable=self.Town, font= ("arial",15, "bold") ,width=32)
        txtTown.grid (row=3, column=3)

        lblAnchal=Label(DataFrameLeft,font=("arial",15,"bold"),text="Anchal/ Thana: ", padx=30,pady=10)
        lblAnchal.grid (row=4, column=2, sticky=W)
        txtAnchal=Entry (DataFrameLeft,textvariable=self.Anchal, font= ("arial", 15, "bold"), width=32)
        txtAnchal.grid(row=4,column=3)

        lblDate=Label(DataFrameLeft,font=("arial",15,"bold"),text="Date: ", padx=30,pady=10)
        lblDate.grid (row=5, column=2, sticky=W)
        txtDate=Entry (DataFrameLeft, textvariable=self.Date,font= ("arial", 15, "bold"), width=32)
        txtDate.grid(row=5,column=3)

        # ========================DataFrameRight=========================
        self.txtVoterInfo= Text(DataFrameRight,font=("arial",15,"bold"),width=64,height=19,pady=5,padx=5)
        self.txtVoterInfo.grid(row=0,column=0)

        # ==========================Buttons==============================

        btnVoterData=Button(Buttonframe,command=self.iVoterInfo,text="VoterID Data",bg="green",fg="white",font=("arial",20,"bold"),width=300,height=40)
        btnVoterData.grid(row=0,column=0)

        btnInsert=Button(Buttonframe,command=self.iVoterData,text="Insert Details",bg="green",fg="white",font=("arial",20,"bold"),width=280,height=40)
        btnInsert.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",20,"bold"),width=270,height=40)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",20,"bold"),width=270,height=40)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.iclear,text="Clear",bg="green",fg="white",font=("arial",20,"bold"),width=270,height=40)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,command=self.iexit,text="Exit",bg="green",fg="white",font=("arial",20,"bold"),width=270,height=40)
        btnExit.grid(row=0,column=5)

        # =============================Table=============================
        # =======================Scrollbar===============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.voterID_table=ttk.Treeview(Detailsframe,columns=("voterID","EName","Gender","HName","FName","DOB","Pincode","State","District","Area","Town","Anchal","Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.voterID_table.xview)
        scroll_y=ttk.Scrollbar(command=self.voterID_table.yview)

        self.voterID_table.heading("voterID",text="VoterID")
        self.voterID_table.heading("EName",text="Elector's Name")
        self.voterID_table.heading("Gender",text="Gender")
        self.voterID_table.heading("HName",text="Husband's Name")
        self.voterID_table.heading("FName",text="Father's Name")
        self.voterID_table.heading("DOB",text="Date Of Birth")
        self.voterID_table.heading("Pincode",text="Pincode")
        self.voterID_table.heading("State",text="State")
        self.voterID_table.heading("District",text="District")
        self.voterID_table.heading("Area",text="Area/ Colony")
        self.voterID_table.heading("Town",text="Town/ Village")
        self.voterID_table.heading("Anchal",text="Anchal/ Thana")
        self.voterID_table.heading("Date",text="Date")

        self.voterID_table["show"]="headings"

        self.voterID_table.column("voterID",width=125)
        self.voterID_table.column("EName",width=150)
        self.voterID_table.column("Gender",width=125)
        self.voterID_table.column("HName",width=150)
        self.voterID_table.column("FName",width=150)
        self.voterID_table.column("DOB",width=125)
        self.voterID_table.column("Pincode",width=125)
        self.voterID_table.column("State",width=125)
        self.voterID_table.column("District",width=125)
        self.voterID_table.column("Area",width=150)
        self.voterID_table.column("Town",width=125)
        self.voterID_table.column("Anchal",width=125)
        self.voterID_table.column("Date",width=125)

        self.voterID_table.pack(fill=BOTH,expand=1)
        self.voterID_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ==================Functionality declaration=======================
   

    def iVoterData(self):
        if self.VoterID.get()=="" or self.EName.get()=="" or self.Gender.get()=="" or self.FName.get()=="" or self.DOB.get()=="" or self.Pincode.get()=="" or self.State.get()==""  or self.District.get()=="" or self.Date.get()==""  :
                messagebox.showerror("Error","Cumpulsory fields cannot be empty")
        else:
            conn=mysql.connector.connect(username='root',password='password',host='localhost',database='Mydata')
            my_cursor=conn.cursor()
            
            sql = ("INSERT INTO VoterID VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            val= (self.VoterID.get(),self.EName.get(),self.Gender.get(),self.HName.get(),self.FName.get(),self.DOB.get(),self.Pincode.get(),self.State.get(),self.District.get(),self.Area.get(),self.Town.get(),self.Anchal.get(),self.Date.get(),)

            my_cursor.execute(sql,val)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(username='root',password='password',host='localhost',database='Mydata')
        my_cursor=conn.cursor()
        sql=("UPDATE VoterID SET ElectorName=%s,Gender=%s,HusbandName=%s,FatherName=%s,DateOfBirth=%s,Pincode=%s,State=%s,District=%s,Area_Colony=%s,Town_Village=%s,Anchal_Thana=%s,Date=%s WHERE VoterID=%s")
        val=(self.EName.get(),self.Gender.get(),self.HName.get(),self.FName.get(),self.DOB.get(),self.Pincode.get(),self.State.get(),self.District.get(),self.Area.get(),self.Town.get(),self.Anchal.get(),self.Date.get(),self.VoterID.get(),)

        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated succesfully")


    def fetch_data(self):
        conn=mysql.connector.connect(username='root',password='password',host='localhost',database='Mydata')
        my_cursor=conn.cursor()
        
        my_cursor.execute("SELECT* from VoterID")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.voterID_table.delete(*self.voterID_table.get_children())
            for i in rows:
                self.voterID_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.voterID_table.focus()
        content=self.voterID_table.item(cursor_row)
        row=content["values"]
        self.VoterID.set(row[0])
        self.EName.set(row[1])
        self.Gender.set(row[2])
        self.HName.set(row[3])
        self.FName.set(row[4])
        self.DOB.set(row[5])
        self.Pincode.set(row[6])
        self.State.set(row[7])
        self.District.set(row[8])
        self.Area.set(row[9])
        self.Town.set(row[10])
        self.Anchal.set(row[11])
        self.Date.set(row[12])
        
                
    def iVoterInfo(self):
        self.txtVoterInfo.insert(END,"VoterID:\t\t"+self.VoterID.get() + 2*"\n")
        self.txtVoterInfo.insert(END,"Elector's Name:\t\t"+self.EName.get() + 2*"\n")
        self.txtVoterInfo.insert(END,"Gender:\t\t"+self.Gender.get() + "\n")
        self.txtVoterInfo.insert(END,"Husband's Name:\t\t"+self.HName.get() + "\n")
        self.txtVoterInfo.insert(END,"Father's Name:\t\t"+self.FName.get() + "\n")
        self.txtVoterInfo.insert(END,"Date Of Birth:\t\t"+self.DOB.get() + 2*"\n")
        self.txtVoterInfo.insert(END,"Pincode:\t\t"+self.Pincode.get() + "\n")
        self.txtVoterInfo.insert(END,"State:\t\t"+self.State.get() + "\n")
        self.txtVoterInfo.insert(END,"District:\t\t"+self.District.get() + "\n")
        self.txtVoterInfo.insert(END,"Area/ Colony:\t\t"+self.Area.get() + "\n")
        self.txtVoterInfo.insert(END,"Town/ Village:\t\t"+self.Town.get() + "\n")
        self.txtVoterInfo.insert(END,"Anchal/ Thana:\t\t"+self.Anchal.get() + 2*"\n")
        self.txtVoterInfo.insert(END,"Date:\t\t"+self.Date.get() + "\n")
        

    def idelete(self):
        conn=mysql.connector.connect(username='root',password='password',host='localhost',database='Mydata')
        my_cursor=conn.cursor()
        sql= "DELETE from VoterID WHERE VoterID=%s"
        val=(self.VoterID.get(),)
        my_cursor.execute(sql,val)
        
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Voter Information deleted Successfully")

        
    def iclear(self):
        self.VoterID.set("")
        self.EName.set("")
        self.Gender.set("")
        self.HName.set("")
        self.FName.set("")
        self.DOB.set("")
        self.Pincode.set("")
        self.State.set("")
        self.District.set("")
        self.Area.set("")
        self.Town.set("")
        self.Anchal.set("")
        self.Date.set("")
        self.txtVoterInfo.delete("1.0",END)

    def iexit(self):
        iexit=messagebox.askyesno("Villager's VoterID Management System","Confirm whether you want to exit or not")
        if iexit>0:
            root.destroy()
            return



root=Tk()
ob=VoterID(root)
root.mainloop()