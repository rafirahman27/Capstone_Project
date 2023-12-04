# imports
import pickle
import streamlit as st

# title
st.title('Vehicle Market Value Estimator')

# production model


# user vehicle information selection
# Make
make = st.selectbox(
    'Manufacturer?',
    ('Abarth', 'Alfa Romeo', 'Audi', 'BMW', 'Citroen', 'Cupra', 'Dacia', 'DS',
    'Fiat', 'Ford', 'Honda', 'Hyundai', 'Infiniti', 'Jaguar', 'Jeep', 'Kia',
    'Land Rover', 'Lexus', 'Maserati', 'Mazda', 'Mercedes-Benz', 'MG',
    'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Renault',
    'Seat', 'Skoda', 'Smart', 'Ssangyong', 'Suzuki', 'Tesla', 'Toyota',
    'Vauxhall', 'Volkswagen', 'Volvo')
)
#Model
if make == 'Abarth':
    st.image('Pictures/abarth-480x270px.jpg', use_column_width = True)
    model = st.selectbox(
        'Model', ('595', '695', '124 Spider')
    )
elif make == 'Alfa Romeo':
    st.image('Pictures/alfa-romeo-720x405px.jpg', use_column_width = True)
    model = st.selectbox(
        'Model', ('Stelvio', 'Giulia')
    )
elif make == 'Audi':
    st.image('Pictures/audi.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('A1','A3','A4','A5','A6','A7','A8','e-tron','Q2','Q3',
         'Q4','Q5','Q7','Q8','TT','A4 Avant','A6 Avant','S5','RS5')
    )
elif make == 'BMW':
    st.image('Pictures/bmw.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('1 Series','2 Series','3 Series','4 Series','5 Series','6 Series','8 Series',
         'X1','X2', 'X3', 'X5','M2','M4','Z4')
    )
elif make == 'Citroen':
    st.image('Pictures/Citroen.jpeg', use_column_width = True)
    model = st.selectbox(
       'Model',
        ('C1','C3','C3 Aircross', 'C4','C4 Spacetourer', 'Grand C4 Spacetourer','C4 Cactus' 
         'C5', 'C5 X', 'C5 Aircross', 'Berlingo')
    )
elif make == 'Cupra':
    st.image('Pictures/cupra.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Leon','Formentor')
    )
elif make =='Dacia':
    st.image('Pictures/dacia.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Duster','Sandero','Sandero Stepway')
    )
elif make =='DS':
    st.image('Pictures/ds.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('DS 3', 'DS 4', 'DS 7')
    )
elif make == 'Fiat':
    st.image('Pictures/fiat.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model', 
        ('500', '500X', 'Panda', 'Tipo Cross')
    )
elif make == 'Ford':
    st.image('Pictures/ford.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Fiesta', 'Focus', 'Kuga', 'Puma', 'Modndeo', 'Ka+', 'Ka', 'Tourneo Courier',
          'Fiesta Vignale','Focus Vignale', 'Mustang', 'C-Max', 'B-Max', 'S-Max', 'Galaxy')
    )
elif make == 'Honda':
    st.image('Pictures/honda.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('CR-V', 'HR-V', 'Jazz', 'Civic')
    )
elif make == 'Hyundai':
    st.image('Pictures/hyundai.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('I10', 'I20', 'I30', 'I40', 'IX20','Ioniq', 'Kona','Tucson',
         'Santa','Bayon')
    )
elif make == 'Infiniti':
    st.image('Pictures/infiniti.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Q30', 'QX30')
    )
elif make == 'Jaguar':
    st.image('Pictures/jaguar.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model', 
        ('XE', 'XF','XJ','E-Pace', 'F-Pace', 'I-Pace')
    )
elif make == 'Jeep':
    st.image('Pictures/jeep.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Renegade', 'Compass')
    )
elif make == 'Kia':
    st.image('Pictures/kia.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Rio', 'Ceed', 'XCeed','Pro Ceed', 'Picanto', 'Niro', 'Sorento', 'Sportage', 'Stonic',
         'Stinger')
    )
elif make == 'Land Rover':
    st.image('Pictures/landrover.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Discovery', 'Discovery Sport', 'Range Rover Evoque', 'Range Rover Velar',
         'Range Rover', 'Range Rover Sport')
    )
elif make == 'Lexus':
    st.image('Pictures/lexus.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('CT', 'ES','IS', 'NX','RC','UX')
    )
elif make == 'Mazda':
    st.image('Pictures/mazda.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('2', '3', '6', 'CX-3','CX-5', 'CX-30','CX-60', 'MX-5')
    )
elif make == 'Mercedes-Benz':
    st.image('Pictures/merc.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('A Class', 'B Class', 'C Class', 'E Class', 'CLA', 'GLA', 'GLB',
         'GLC', 'EQA','EQB','EQC')
    )
elif make == 'MG':
    model = st.selectbox(
        'Model',
        ('MG3', 'ZS', 'HS', 'GS', 'MG5')
    )
elif make == 'Mini':
    st.image('Pictures/mini.JPG', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Hatchback', 'Hatch', 'Countryman', 'Clubman', 'Convertible')
    )
elif make == 'Mitsubishi':
    st.image('Pictures/mitsub.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Eclipse','Eclipse Cross', 'ASX', 'Mirage', 'Outlander')
    )
elif make == 'Nissan':
    st.image('Pictures/nissan.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Juke','Qashqai', 'X-Trail', 'Micra','Leaf','E-Nv200')
    )
elif make == 'Peugeot':
    st.image('Pictures/peugeot.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('108','208', '2008', '308', '3008', '508', '5008')
    )
elif make == 'Porsche':
    st.image('Pictures/porsche.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Panamera', 'Caymane', 'Macan')
    )
elif make == 'Renault':
    st.image('Pictures/renault.JPG', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Arkana', 'Clio','Captur','Kadjar','Megane','Twingo', 'ZOE')
    )
elif make == 'Seat':
    st.image('Pictures/seat.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Arona','Ateca','Cupra Ateca', 'Ibiza','Leon','Toledo','Tarraco')
    )
elif make == 'Skoda':
    st.image('Pictures/skoda.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Citigo','Fabio','Karoq','Kodiaq','Octavia','Rapid','Scala','Superb')
    )
elif make == 'Smart':
    st.image('Pictures/smart.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Fortwo', 'ForFour')
    )
elif make == 'Ssangyong':
    st.image('Pictures/ssangyong.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Korando', '')
    )
elif make == 'Suzuki':
    st.image('Pictures/suzuki.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Across','Baleno','Celerio','Ignis','Jimny','S-Cross', 'Swace','Swift','SX4-Cross', 'Vitara')
    )
elif make == 'Telsa':
    st.image('Pictures/tesla.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Model 3', '')
    )
elif make == 'Toyota':
    st.image('Pictures/toyota.JPG', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Aygo', 'Aygo X', 'C-HR', 'Corolla','Highlander','Gr Yaris','Gr Supra','RAV4','Yaris','Yaris Cross')
    )
elif make == 'Vauxhall':
    st.image('Pictures/vauxhall.jpg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Adam','Astra', 'Astra GTC', 'Corsa','Crossland','Crossland X', 'Grandland', 'Grandland X',
         'Insignia','Meriva', 'Mokka', 'Mokka X','Viva')
    )
elif make == 'Volkswagen':
    st.image('Pictures/vw.JPG', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('Golf','Polo','Tiguan','T-Roc','T-Cross','Touareg','Passat','Taigo','Arteon','Up',
         'Caddy','Touran','Scirocco','Sharan','e-Golf')
    )
else:
    st.image('Pictures/volvo.jpeg', use_column_width = True)
    model = st.selectbox(
        'Model',
        ('V40', 'V60', 'S60', 'XC40', 'XC60','XC90')
    )


#Trim 
if make == 'Abarth':
    trim1 = st.selectbox(
        'Trim',
        ('T-Jet', '')
    )
    trim2 = st.selectbox(
        'Version',
        ('Standard','Competizione', 'Turismo','F9','Trofeo','7th Anniversary',
         'Turismo 7th Anniversary')
    )
elif make == 'Alfa Romeo':
    trim1 = st.selectbox(
        'Trim',
        ('Speciale Auto','Veloce Auto')
    )
elif make == 'Audi':
    trim1 = st.selectbox(
        'Trim',
        ('TFSI', 'TDI', 'FSI','25 TFSI', '30 TFSI','35 TFSI', '40 TFSI', '45 TFSI','50 TFSI',
         '55 TFSI','30 TDI','35 TDI', '40 TDI', '45 TDI','50 TDI','50 Quattro',
         '55 Quattro', 'GT Quattro', 'S3')
    )
    trim2 = st.selectbox(
        'Version',
        ('Standard','S Line','S Line S Tronic','Sport','95 Blac Ed Auto','Quattro S Line','TFSI Quattro  S Tronic',
         'Tecni', 'Blac Edition','Quattro Blac Edition S Tronic')
    )
if make == 'BMW':
    trim1 = st.selectbox(
        'Trim',
        ('116d', '116i', '118d', '118i', '120i', '120d', '125d','M135i', 'M140i',
         '218i', '218d','220i', '220d', '2208i', '230i','M240i', 'M235i','M2',
         '318i', '318d','320i', '320d', '330d', '330i', '330e','340i', '340d','M3',
         '420i', '420d', '430d', '430i', '435d','440i','M4',
         '520i', '520d', '530d', '530i', '530e','540i','M5',
         '18i','18d','20i','20d'
         
         )
    )
    trim2 = st.selectbox(
        'Version',
        ('SE','SE DCT', 'Sport', 'M Sport','M Sport Shadow Edition', 'M Sport Auto','M Sport DCT', 
         'SE Business [Nav-Servotronic]', 'M Sport  Step Auto [LCP-Pro pk]','Step Auto [Pro Pack]',
         'Step Auto [Live Cockpit Professional]','Shadow Edition Auto','M Sport [Live Cockpit Pro-Pro pk]',
         'M Sport [Nav] Step Auto','M Sport DCT', 'SE Touring','Sport Touring','7.6kWh SE Auto',
         '7.6kWh M Sport Auto', 'M Sport Shadow Edition Auto xDrive', 'M Sport  Auto [Professional Media]',
         '9.2kWh SE Auto','12kWh SE Auto','DCT [Competition-Ultimate Pack]','DCT [Competition Pack]','Active Tourer',
         'Gran Coupe','Gran Tourer','Gran Turismo'  )
    )
elif make == 'Citroen':
    trim1 = st.selectbox(
        'Trim',
        ('PureTech','BlueHDi','VTi','Plug-in Hybrid')
    )
    trim2 = st.selectbox(
        'Version',
        ('Flair','Flair Plus','Shine','Shine Plus','PureTec Sine Plus','C-Series Edition','Sense Plus')
    )
elif make == 'Cupra':
    trim1 = st.selectbox(
        'Trim',
        ('eTSI DSG', 'eHybrid DSG')
    )
elif make == 'Dacia':
    trim1 = st.selectbox(
        'Trim',
        ('SCe', 'TCe', 'SCe Bi-Fuel','TCe Bi-Fuel')
    )
    trim2 = st.selectbox(
        'Version',
        ('Essential', 'Comfort','SE Twenty','Prestige','Ambiance','Techroad','Journey EDC',
         'Laureate','Extreme')
    )
elif make == 'DS':
    trim1 = st.selectbox(
        'Trim',
        ('E-Tense','PureTech','BlueHDi')
    )
    trim2 = st.selectbox(
        'Version',
        ('Elegance','Prestige','Performance Line','Chic','4x4 Performance Line','Ultra Prestige')
    )
elif make == 'Fiat':
    trim1 = st.selectbox(
        'Trim',
        ('Mild Hybrid Dolcevita','Mild Hybrid Roc Star','Mild Hybrid Lounge','Lounge','Lounge Dualogic',
         'Star','Sport','Pop Dualogic','Easy','E-torQ Pop','Lounge','MHEV Sport','MHEV Star','Mild Hybrid Sport',
         'TwinAir Lounge','Sport DCT','MHEV Lounge','Collezione Fall','City Cross','Hybrid 48V Sport DDCT'
         )
    )
elif make == 'Ford':
    trim1 = st.selectbox(
        'Trim',
        ('EcoBoost','Titanium', 'Vignale','Zetec','ST-Line','Trend','EcoBlue','V8')
    )
    trim2 = st.selectbox(
        'Trim',
        ('Titanium','Titanium X' 'ST-Line','Hybrid ST-Line Edition', 'Active','Active Edition',
         'TDCi','Vignale','RS 23','95 Active X Edition','ST','Zetec S','GTT [Custom Pack]',
         'Bullitt','GT Shadow Edition')
    )
elif make == 'Honda':
    trim1 = st.selectbox(
        'Trim',
        (
           'i-DTEC SE','i-MMD Hybrid SR eCVT','VTE Turbo EX VT','VTE Turbo SR','VTE Turbo Sport',
           'VTE Turbo Sport Plus VT','i-VTE EX Navi','i-VTE SR','i-VTE SE Plus','i-VTEC S','VTEC Turbo  SE' 
        )
    )
elif make == 'Hyundai':
    trim1 = st.selectbox(
        'Trim',
        (
            'GDi Hybrid Premium DT','GDi SE Nav WD','GDi SE Nav','CRDi SE Nav','MPi Premium',
            'TGDi Hybrid N Line S','MPi SE connect','TGDi SE connect','GDi SE Nav','Premium SE',
            'T GDi 8V MHD Ultimate','TGDi N Line','GDi Hybrid Premium SE DT','Fe TGDi Hybrid Ultimate'
       )
    )
elif make == 'Infiniti':
    trim1 = st.selectbox(
        'Trim',
        (
            'Premium Tech DCT', ''
        )
    )
elif make == 'Jaguar':
    trim1 = st.selectbox(
        'Trim',
        (
            'D150','D165','D180','D200','D240','D300','P180','P200','P250','R','V6'
        )
    )
    trim2 = st.selectbox(
        'Version',
        (
            'R-Sport','Portfolio','SE','Chequered Flag','R-Dynamic','R-Dynamic S', 'S',
            'R-Sport AWD','Portfolio AWD','SE AWD','Chequered Flag AWD','R-Dynamic AWD','R-Dynamic S AWD','S AWD'
            'V6 Portfolio','V6 Portfolio AWD', 'Supercharged', 'Supercharged AWD'
            
        )
    )
elif make == 'Jeep':
    trim1 == st.selectbox(
        'Trim',
        (
            'T3 GSE Limited','T3 GSE Night Eagle II','T4 GSE Night Eagle','Turbo 4xe PHEV Limited',
            'Multijet Limited DDT','Multiair Longitude'
        )
    )
elif make == 'Kia':
    trim1 = st.selectbox(
        'Trim',
        (
            'GDi','T GDi','RDi','CRDi'
        )
    )
    trim2 = st.selectbox(
        'Version',
        (
            'ISG','ISG GT-Line','ISG Platinum Edition', 'HEV GT-Line S','GT-Line S DT','ISG Platinum Edition',
            '8V ISG GT-Line','GT-Line'
        )
    )
elif make == 'Land Rover':
    trim1 = st.selectbox(
        'Trim',
        (
            'TD4 SE Tech Auto 4WD','eD4 SE Tech FWD','TD4 SE Tech 4WD','TD4 HSE Dynamic Auto 4WD','TD4 HSE Auto 4WD',
            'TD4 SE 4WD','SD4 HSE Dynamic Auto 4WD','TD4 Landmark Auto 4WD','D R-Dynamic HSE  Auto','D150 S FWD',
            'TD4 Landmark 4WD'       
        )
    )
elif make == 'Lexus':
    trim1 = st.selectbox(
        'Trim',
        (
            'F-Sport  VT [Premium Pac/Leater]','Takumi CVT','CVT','F-Sport CVT','F-Sport CVT [Nav]','Executive Edition CVT Auto',
            'CVT [Nav]','F-Sport CVT [Premium assist]'
        )
    )
elif make == 'Maserati':
    trim1 = st.selectbox(
        'Trim',
        (
          'V6d Auto', ''  
        )
    )
elif make == 'Mazda':
    trim1 = st.selectbox(
        'Trim',
        (
            'Sport Nav','Syactiv X MHEV Sport Lux','Syactiv G MHEV SE-L Lux','PHEV Homura Auto','Exclusive Line Auto','GT Sport Tec',
            'e-Syactiv G MHEV SE-L Lux','GT Sport Nav\u002B','Syactiv-X MHEV GT Sport Tec  Auto AD','Sport Lux Auto','Syactiv-G MHEV Sport Lux',
            'Homura','Syactiv G GT Sport Auto','e-Syactiv G MHEV GT Sport Tec','Sport Blac','Syactiv G SE-L Nav'         
        )
    )
elif make == 'Mercedes-Benz':
    trim1 = st.selectbox(
        'Trim',
        (
            'A180', 'A180d', 'A200','A200d','A250e','B180','B180d','B200','B200d','C180','C180d','C200','C200d',
            'C220d', 'C300','C300d','C350e','C43','C63','200','200d','180','180d','43','63'
        )
    )
    trim2 = st.selectbox(
        'Version',
        (
            'AMG Line', 'AMG Line Executive','AMG Line Premium','Sport Executive','Sport','Urban Edition',
            '15.6kWh AMG Line 8G-DCT','AMG Line Night Edition'
        )
    
    )
elif make == 'MG':
    trim1 = st.selectbox(
        'Trim',
        (
            'VTi-TEH Excite','VTi-TEH Exclusive','Exclusive EV 6dr Auto','Excite EV 5 Auto'
        )
    )
elif make == 'Mini':
    trim1 = st.selectbox(
        'Trim',
        (
            'Cooper','Cooper Classic','Cooper S', 'JCW'
        )
    )
    trim2 = st.selectbox(
        'Version',
        (
            'Classic','Classic II','Sport','Sport II','Exclusive','Exclusive II','John Cooper Works',
            'Classic [Comfort Pack]','Classic II [Comfort Pack]','Sport [Comfort Pack]','Sport II [Comfort Pack]','Exclusive [Comfort Pack]','Exclusive II [Comfort Pack]','John Cooper Works [Comfort Pack]',
            'Classic [Comfort-Nav Pack]','Classic II [Comfort-Nav Pack]','Sport [Comfort-Nav Pack]','Sport II [Comfort-Nav Pack]',
            'Exclusive [Comfort-Nav Pack]','Exclusive II [Comfort-Nav Pack]','John Cooper Works [Comfort-Nav Pack]',
            
        )
    )
elif make == 'Mitsubishi':
    trim1 = st.selectbox(
        'Trim',
        (
            'Dynamic', 'Design','Black','Juro','Design CVT','Exceed CVT','Exceed CVT 4WD','Exceed'  
        )
    )
elif make == 'Nissan':
    trim1 = st.selectbox(
        'Trim',
        (
            'Acenta', 'Acenta Premium', 'Bose Personal Edition', 'Design', 'Design CVT', 'DiG-T',
            'DiG-T Acenta Premium', 'DiG-T MH Acenta Premium', 'DiG-T MH Acenta Premium Xtronic',
            'DiG-T N-Connecta', 'DiG-T N-Motion', 'DiG-T N-onnecta DT', 'DiG-T N-Tec DT', 'DiG-T Tena',
            'DiG-T Tena DT', 'DiG-T Tena Xtronic', 'dCi Acenta Premium', 'dCi Visia', 'Exceed',
            'Exceed CVT', 'Exceed CVT 4WD', 'Glass Roof Pack', 'IG-T', 'IG-T 9 Acenta', 'IG-T 9 N-Sport',
            'IG-T 9 N-Sport CVT [Nav]', 'Juro', 'N-Connecta', 'N-Motion', 'N-Tec DT', 'N-Vision', 'Personal Edition',
            'Premium', 'Tekna', 'Tena', 'Visia', 'Xtronic'
        )
    )
elif make == 'Peugeot':
    trim1 = st.selectbox(
        'Trim',
        (
            'Active', 'Allure', 'Allure Premium', 'GT', 'GT Line', 'Active Premium', 'GT Premium',
            'Tech Edition', 'GT Line Premium', 'Allure -Tronic', 'Hybrid4 GT', 'Hybrid GT',
            'Hybrid4 GT Premium', 'BlueHDi'
        )
    )
elif make == 'Porsche':
    trim1 = st.selectbox(
        'Trim',
        (
            'V8 Turbo GTS PDK', 'PDK'
        )
    )
elif make == 'Renault':
    trim1 = st.selectbox(
        'Trim',
        (
            'TCe S Edition', 'dCi Iconic', 'dCi ENERGY Dynamique S Nav', 'i Iconic R 50 Rapid Charge Auto',
            'E-TEH Hybrid S Edition Auto', 'TE S Edition ED', 'Te 90 RS Line', 'TE GT Line', '80 Play R 50 Auto',
            'TE Iconic', 'TE 90 GT Line', 'TE 90 EO Dynamique Nav', 'i GT Line R 50 Rapid Charge Auto', 'TCe 9 GT Line',
            'dCi ENERGY Play', 'TCe ENERGY Iconic', 'TCe 9 Iconic', 'TCe S Edition EDC', 'dCi 9 Iconic', 'TCe RS Line',
            'TCe GT Line', 'TCe Dynamique S Nav', 'TCe 9 S Edition', 'dCi 9 Dynamique Nav', 'dCi 9 GT Line',
            'TCe RS Line EDC', 'SCe 7 Play', 'kW i Iconic R kWh Rapid Charge Auto', 'E-TECH Hybrid RS Line Auto',
            'TCe 9 Play', 'TCe GT Line EDC', 'E-TECH full hybrid Techno Auto', 'TCe RS Line [Bose]', 'TCe 9 RS Line',
            'TCe Dynamique Nav', 'dCi 9 Dynamique S Nav', 'E-TECH Hybrid S Edition Auto', 'Blue dCi GT Line Auto',
            'Mild hybrid RS Line EDC', 'E-TECH PHEV S Edition Auto', 'TCe 9 Iconic Edition', 'TCe ENERGY Dynamique S Nav',
            'SCE Iconic [Start Stop]', 'TCe Play', 'TCe Iconic EDC', 'TCe 9 Lutecia SE'
        )
    )
#'Seat', 'Skoda', 'Smart', 'Ssangyong', 'Suzuki', 'Tesla', 'Toyota','Vauxhall', 'Volkswagen', 'Volvo'
elif make == 'Seat' or make == 'Skoda':
    trim1 = st.selectbox(
        'Trim',
        (
            'TSI SE Technology', 'TSI FR [EZ]', 'MPI SE Technology', 'EcoTSI SE ST', 'TSI XCELLENCE', 'TSI EVO SE Dynamic',
            'TSI FR Sport', 'TSI EVO FR', 'TSI FR Technology Sport', 'TSI EVO SE Technology', 'TSI Fort [EZ]', 'TSI SE Technology DSG', 
            'TSI SE Dynamic [EZ]', 'TSI Xcellence Lux [EZ] DSG', 'TSI 9 Xcellence [EZ]', 'TSI EVO SE Dynamic [EZ]', 'TSI EVO SE Technology [EZ]', 
            'TSI EVO FR [EZ]', 'TSI Fort', 'TSI FR Red Edition', 'TSI FR Edition', 'TSI 9 FR', 'SE Technology [EZ]', 'TSI DSG', 'TSI 9 Xcellence', 
            'TSI Ecomotive SE [EZ]', 'TSI EVO Xcellence [EZ]', 'TSI Fort [EZ] DSG', 'TSI Cupra [EZ] DSG', 'TSI EVO FR Black Edition [EZ]', 
            'TSI SE Technology [EZ]', 'TSI EVO Xperience', 'TSI EVO SE Technology DSG', 'TSI FR [EZ] DSG', 'TSI 9 Xcellence Lux', 'TSI Xcellence Lux [EZ] DSG', 
            'TSI EVO Xcellence Lux [EZ]', 'TSI EVO SE [EZ]', 'TSI Xcellence', 'TSI EVO FR', 'TSI DSG [Comfort -Plus Sound pack]', 'TDI Xcellence', 
            'TDI Ecomotive SE', 'Fort [EZ]', 'TSI EVO Fort', 'TSI SE Dynamic Technology', 'TSI Ecomotive SE Technology [EZ]', 'TDI Xcellence [EZ]', 'TSI EVO Fort [EZ] DSG', 
            'TSI EVO FR [EZ] DSG', 'TSI FR Edition DSG', 'Toca Sport Euro 5', '12v Mii by Cosmopolitan'
        )
    )
elif make == 'Smart':
    trim1 = st.selectbox(
        'Trim',
        (
            'Prime Sport (Premium) Twinamic','Prime (Premium) Twinamic','Passion Twinamic','Prime','Pure','Edition 1'    
        )
    )
elif make == 'Ssangyong':
    trim1 = st.selectbox(
        'Trim',
        (
            'D Ultimate 4x4 Auto','Ultimate','Ventura','Ultimate 4x4 Auto' 
        )
    )
elif make == 'Suzuki':
    trim1 = st.selectbox(
        'Trim',
        (
           'Boosterjet SZ-T', 'Boosterjet 8V Hybrid SZ5 ALLGRIP', 'Dualjet SHVS SZ-T', 'Boosterjet 8V Hybrid SZ-T', 'Boosterjet 48V Hybrid Sport', 'Boosterjet S ALLGRIP Auto', 
           'Dualjet Adventure', 'Hybrid SZ5 ALLGRIP AGS', 'Boosterjet 8V Hybrid Sport', 'Dualjet SZ-T Auto', 'Dualjet 83 12V Hybrid SZ-L', 'Boosterjet 8V Hybrid Motion', 'Hybrid SZ5 VT', 
           'PHEV E-Four VT', 'Dualjet 83 12V Hybrid SZ-T', 'Boosterjet SZ-T Auto', 'Boosterjet 48V Hybrid SZ-T', 'Dualjet SHVS SZ', 'Dualjet 83 V Hybrid SZ-T Auto', 'SZ4', 'Boosterjet SZ-T', 
           'Dualjet SZ3', 'Dualjet SZ-T', 'Boosterjet 48V Hybrid Motion Auto', 'Dualjet 83 V Hybrid SZ-L', 'Boosterjet SZ Auto', 'SZ ALLGRIP', 'Dualjet 83 V Hybrid SZ-T', 'Boosterjet SZ', 'SZ-T', 
           'Boosterjet 48V Hybrid SZ ALLGRIP Auto', 'Hybrid SZ CVT' 
        )
    )
elif make == 'Telsa':
    trim1 = st.selectbox(
        'Trim',
        (
            'Standard Plus Auto','3 Performance AD [Performance Upgrade] Auto'
        )
    )
elif make == 'Toyota':
    trim1 = st.selectbox(
        'Trim',
        (
            'Hybrid Design VT','VVT-i X-Play','Hybrid Icon CVT','VVT-i X-Trend','VVT-i Hybrid Design VT','Hybrid Dynamic VT',
            '3 VVT-i Design','Cross Hybrid Design VT','Hybrid Icon VT','VVT-i X-lusiv x-sift','VVT-i x-play','VVT-i Hybrid Gort CVT',
            'Hybrid Design CVT','Dual VVT-i Icon','VVT-i Icon Tech','VVT-i Hybrid Excel CVT','Hybrid Dynamic CVT','VVT-i Hybrid Design CVT',
            'VVT-i X-Trend TSS','VVT-i X-Trend  x-shift','VVT-i Hybrid Icon Tech  CVT','AWD [Circuit Pack]','VVT-i X-Trend TSS  x-shift',
            'VVT-i Hybrid Design  CVT WD','VVT-i X-Play TSS','PHEV Dynamic  CVT','T Icon','VVT-i Icon','VVT-i X-Plore','Hybrid Excel  CVT',
            'VVT-i Pure Auto','VVT-i Hybrid Excel CVT WD'            
        )
    )
elif make == 'Vauxhall':
    trim1 = st.selectbox(
        'Trim',
        (
            'Turbo SRi Premium','Turbo SRi Nav Premium','Turbo Tech Line 2WD','CDTi Tech Line 2WD','Turbo Elite Nav Auto','CDTi ecoTEC D Active',
            'Turbo Griffin','Turbo SRi Nav','X Turbo SRi Nav Auto [8 Speed]','X T ecoTE Elite Nav','SE','Turbo SRi','Turbo Elite Nav Premium',
            'SE Nav','Turbo Elite Nav','[83] Griffin [Start Stop]','T 16V SRi Nav','Turbo Ultimate Auto','X Turbo Sport Nav','SRi Nav Premium 50 Auto []',
            'X T Design Nav','[83] SRi Nav [Start Stop]','Turbo SE','SE Premium','Turbo Elite Nav Premium Auto','Turbo D SRi Nav Auto',
            'Turbo SE Nav Premium Auto','[83] Elite Nav','SE Nav Premium 50 Auto []','Turbo D Business Edition','X Turbo Elite Nav',
            'Elite Premium 50 Auto','X Hybrid Ultimate Nav Auto','Turbo D Business Edition Nav','X T ecoTE Design Nav','Elite Nav Premium 50 Auto',
            'Turbo D Elite Nav Auto','Turbo D Ultimate Nav','SRi Nav Premium 50 Auto','Launc Edition 50 Auto',
        )
    )
elif make == 'Volkswagen':
    trim1 = st.selectbox(
        'Trim',
        (
           'TSI','eTSI','TDI','EVO','GTI','R','V6 TSI', 'V6 TDI' 
        )
    )
    trim2 = st.selectbox(
        'Version',
        (
            'Life','80 Match','R-Line','R-Motion','Design','EVO R-Line','EVO Match Edition','SE','Motion SEL Tec Tip','Motion Black Edition',
            'Style','GT','GT DSG','80 Beats','Motion R-Line', 'GTD DSG','Pro Performance','GTI Performance','Business Pro Performance'
        )
    )
elif make == 'Volvo':
    trim1 = st.selectbox(
        'Trim',
        (
            'BP R DESIGN Pro AD Auto','T3 Inscription','B4P Plus Dark Geartronic','B3P Core Auto','T Inscription Plus Auto','BP Momentum AWD Gtron',
            'D3 Momentum','B3P Plus Dark Auto','T3 Momentum','T3 R DESIGN Pro Geartronic','BP Inscription Auto','T3 R DESIGN Edition Geartronic',
            'T First Edition AWD Geartronic','D4 Inscription AWD Geartronic','T3 Inscription Pro','T Inscription Auto'
        )
    )
# Engine size
if trim2 is not None:
    trim = trim1 + ' ' + trim2
else:
    trim = trim1
if make is not None and model is not None and trim is not None:
    engine_size = st.selectbox(
        'Engine Size',
        ('0.0', '1.0', '1.1', '1.2', '1.25', '1.3', '1.33', '1.4', '1.5', '1.6',
         '1.7', '1.8', '2.0', '2.1', '2.2', '2.3', '2.5', '2.9', '3.0', '3.3', '3.5',
         '5.0', '6.2')
    )

# Mileage
if engine_size is not None:
    mileage = st.number_input('Mileage:', min_value=0, step=1)
#number of doors
    if mileage > 15:
         num_doors = st.selectbox(
            'Number of Doors',
            ('2', '3', '4', '5')
    )
else:
    st.write('Please Enter mileage to continue')
#gearbox
if num_doors is not None:
        gearbox = st.selectbox(
            'Transmission',
            ('Manual', 'Automatic', 'Semiauto')
    )
#reg_yea
if gearbox is not None:
    reg_year = st.number_input('Year of Registration:', min_value=2000, step=1)