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
    model = st.selectbox(
        'Model', ('595', '695', '124 Spider')
    )
elif make == 'Alfa Romeo':
    model = st.selectbox(
        'Model', ('Stelvio', 'Giulia')
    )
elif make == 'Audi':
    model = st.selectbox(
        'Model',
        ('A1','A3','A4','A5','A6','A7','A8','e-tron','Q2','Q3',
         'Q4','Q5','Q7','Q8','TT','A4 Avant','A6 Avant','S5','RS5')
    )
elif make == 'BMW':
    model = st.selectbox(
        'Model',
        ('1 Series','2 Series','3 Series','4 Series','5 Series','6 Series','8 Series',
         'X1','X2', 'X3', 'X5','M2','M4','Z4')
    )
elif make == 'Citroen':
    model = st.selectbox(
       'Model',
        ('C1','C3','C3 Aircross', 'C4','C4 Spacetourer', 'Grand C4 Spacetourer','C4 Cactus' 
         'C5', 'C5 X', 'C5 Aircross', 'Berlingo')
    )
elif make == 'Cupra':
    model = st.selectbox(
        'Model',
        ('Leon','Formentor')
    )
elif make =='Dacia':
    model = st.selectbox(
        'Model',
        ('Duster','Sandero','Sandero Stepway')
    )
elif make =='DS':
    model = st.selectbox(
        'Model',
        ('DS 3', 'DS 4', 'DS 7')
    )
elif make == 'Fiat':
    model = st.selectbox(
        'Model', 
        ('500', '500X', 'Panda', 'Tipo Cross')
    )
elif make == 'Ford':
    model = st.selectbox(
        'Model',
        ('Fiesta', 'Focus', 'Kuga', 'Puma', 'Modndeo', 'Ka+', 'Ka', 'Tourneo Courier',
          'Fiesta Vignale','Focus Vignale', 'Mustang', 'C-Max', 'B-Max', 'S-Max', 'Galaxy')
    )
elif make == 'Honda':
    model = st.selectbox(
        'Model',
        ('CR-V', 'HR-V', 'Jazz', 'Civic')
    )
elif make == 'Hyundai':
    model = st.selectbox(
        'Model',
        ('I10', 'I20', 'I30', 'I40', 'IX20','Ioniq', 'Kona','Tucson',
         'Santa','Bayon')
    )
elif make == 'Infiniti':
    model = st.selectbox(
        'Model',
        ('Q30', 'QX30')
    )
elif make == 'Jaguar':
    model = st.selectbox(
        'Model', 
        ('XE', 'XF','XJ','E-Pace', 'F-Pace', 'I-Pace')
    )
elif make == 'Jeep':
    model = st.selectbox(
        'Model',
        ('Renegade', 'Compass')
    )
elif make == 'Kia':
    model = st.selectbox(
        'Model',
        ('Rio', 'Ceed', 'XCeed','Pro Ceed', 'Picanto', 'Niro', 'Sorento', 'Sportage', 'Stonic',
         'Stinger')
    )
elif make == 'Land Rover':
    model = st.selectbox(
        'Model',
        ('Discovery', 'Discovery Sport', 'Range Rover Evoque', 'Range Rover Velar',
         'Range Rover', 'Range Rover Sport')
    )
elif make == 'Lexus':
    model = st.selectbox(
        'Model',
        ('CT', 'ES','IS', 'NX','RC','UX')
    )
elif make == 'Mazda':
    model = st.selectbox(
        'Model',
        ('2', '3', '6', 'CX-3','CX-5', 'CX-30','CX-60', 'MX-5')
    )
elif make == 'Mercedes-Benz':
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
    model = st.selectbox(
        'Model',
        ('Hatchback', 'Hatch', 'Countryman', 'Clubman', 'Convertible')
    )
elif make == 'Mitsubishi':
    model = st.selectbox(
        'Model',
        ('Eclipse','Eclipse Cross', 'ASX', 'Mirage', 'Outlander')
    )
elif make == 'Nissan':
    model = st.selectbox(
        'Model',
        ('Juke','Qashqai', 'X-Trail', 'Micra','Leaf','E-Nv200')
    )
elif make == 'Peugeot':
    model = st.selectbox(
        'Model',
        ('108','208', '2008', '308', '3008', '508', '5008')
    )
elif make == 'Porsche':
    model = st.selectbox(
        'Model',
        ('Panamera', 'Caymane', 'Macan')
    )
elif make == 'Renault':
    model = st.selectbox(
        'Model',
        ('Arkana', 'Clio','Captur','Kadjar','Megane','Twingo', 'ZOE')
    )
elif make == 'Seat':
    model = st.selectbox(
        'Model',
        ('Arona','Ateca','Cupra Ateca', 'Ibiza','Leon','Toledo','Tarraco')
    )
elif make == 'Skoda':
    model = st.selectbox(
        'Model',
        ('Citigo','Fabio','Karoq','Kodiaq','Octavia','Rapid','Scala','Superb')
    )
elif make == 'Smart':
    model = st.selectbox(
        'Model',
        ('Fortwo', 'ForFour')
    )
elif make == 'Ssangyong':
    model = st.selectbox(
        'Model',
        ('Korando', '')
    )
elif make == 'Suzuki':
    model = st.selectbox(
        'Model',
        ('Across','Baleno','Celerio','Ignis','Jimny','S-Cross', 'Swace','Swift','SX4-Cross', 'Vitara')
    )
elif make == 'Telsa':
    model = st.selectbox(
        'Model',
        ('Model 3', '')
    )
elif make == 'Toyota':
    model = st.selectbox(
        'Model',
        ('Aygo', 'Aygo X', 'C-HR', 'Corolla','Highlander','Gr Yaris','Gr Supra','RAV4','Yaris','Yaris Cross')
    )
elif make == 'Vauxhall':
    model = st.selectbox(
        'Model',
        ('Adam','Astra', 'Astra GTC', 'Corsa','Crossland','Crossland X', 'Grandland', 'Grandland X',
         'Insignia','Meriva', 'Mokka', 'Mokka X','Viva')
    )
elif make == 'Volkswagen':
    model = st.selectbox(
        'Model',
        ('Golf','Polo','Tiguan','T-Roc','T-Cross','Touareg','Passat','Taigo','Arteon','Up',
         'Caddy','Touran','Scirocco','Sharan','e-Golf')
    )
else:
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
if make == 'Alfa Romeo':
    trim1 = st.selectbox(
        'Trim',
        ('Speciale Auto','Veloce Auto')
    )
if make == 'Audi':
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

#  'Citroen', 'Cupra', 'Dacia', 'DS', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Infiniti', 'Jaguar', 'Jeep', 'Kia',
if make == 'Citroen':
    trim1 = st.selectbox(
        'Trim',
        ('PureTech','BlueHDi','VTi','Plug-in Hybrid')
    )
    trim2 = st.selectbox(
        'Version',
        ('Flair','Flair Plus','Shine','Shine Plus','PureTec Sine Plus','C-Series Edition','Sense Plus')
    )
if make == 'Cupra':
    trim1 = st.selectbox(
        'Trim',
        ('eTSI DSG', 'eHybrid DSG')
    )
if make == 'Dacia':
    trim1 = st.selectbox(
        'Trim',
        ('SCe', 'TCe', 'SCe Bi-Fuel','TCe Bi-Fuel')
    )
    trim2 = st.selectbox(
        'Version',
        ('Essential', 'Comfort','SE Twenty','Prestige','Ambiance','Techroad','Journey EDC',
         'Laureate','Extreme')
    )
if make == 'DS':
    trim1 = st.selectbox(
        'Trim',
        ('E-Tense','PureTech','BlueHDi')
    )
    trim2 = st.selectbox(
        'Version',
        ('Elegance','Prestige','Performance Line','Chic','4x4 Performance Line','Ultra Prestige')
    )
if make == 'Fiat':
    trim1 = st.selectbox(
        'Trim',
        ('Mild Hybrid Dolcevita','Mild Hybrid Roc Star','Mild Hybrid Lounge','Lounge','Lounge Dualogic',
         'Star','Sport','Pop Dualogic','Easy','E-torQ Pop','Lounge','MHEV Sport','MHEV Star','Mild Hybrid Sport',
         'TwinAir Lounge','Sport DCT','MHEV Lounge','Collezione Fall','City Cross','Hybrid 48V Sport DDCT'
         )
    )


# Engine size
trim = trim1 + ' ' + trim2
if make is not None and model is not None and trim is not None:
    engine_size = st.selectbox(
        'Engine Size',
        ['0.0', '1.0', '1.1', '1.2', '1.25', '1.3', '1.33', '1.4', '1.5', '1.6',
         '1.7', '1.8', '2.0', '2.1', '2.2', '2.3', '2.5', '2.9', '3.0', '3.3', '3.5',
         '5.0', '6.2']

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
#reg_year
if gearbox is not None:
    reg_year = st.number_input('Year of Registration:', min_value=2000, step=1)