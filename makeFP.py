import lxml.etree as ET

with open('recipes.js', 'r') as f:
    data = f.read()
    data = data[223:]
    data = data.replace('export default [', '[')
    data = data.replace('];', ']')
    data = eval(data)

for i in data:
    if i['sensor'] != 4:
        continue
    sample = ET.parse('sample.FP1')
    root = sample.getroot()
    target_tag = root.find("PropertyGroup")
    i['name'] = i['name'].replace('/', 'slash')
    target_tag.set('label', str(i['name']+' by '+i['creator']))
    # ExposureBias
    if i['ev'] == '+1/1':
        target_tag.find('ExposureBias').text =  'P1P00'
    elif i['ev'] == '+2/3':
        target_tag.find('ExposureBias').text =  'P0P67'
    elif i['ev'] == '+1/3':
        target_tag.find('ExposureBias').text =  'P0P33'
    elif i['ev'] == '0':
        target_tag.find('ExposureBias').text =  'P0P00'
    elif i['ev'] == '-1/3':
        target_tag.find('ExposureBias').text =  'M0P33'
    elif i['ev'] == '-2/3':
        target_tag.find('ExposureBias').text =  'M0P67'
    elif i['ev'] == '-1/1':
        target_tag.find('ExposureBias').text =  'M1P00'
    
    # DynamicRange
    if i['dr'] == 'AUTO':
        target_tag.find('DynamicRange').text = ''
    else:
        target_tag.find('DynamicRange').text = str(i['dr'].replace('DR', ''))
    
    # FilmSimulation
    if i['film'] == 'PROVIA/Standard':
        target_tag.find('FilmSimulation').text = 'Provia'
    elif i['film'] == 'VELVIA/Vivid':
        target_tag.find('FilmSimulation').text = 'Velvia'
    elif i['film'] == 'ASTIA/Soft':
        target_tag.find('FilmSimulation').text = 'Astia'
    elif i['film'] == 'Classic Chrome':
        target_tag.find('FilmSimulation').text = 'Classic'
    elif i['film'] == 'Pro Neg Hi':
        target_tag.find('FilmSimulation').text = 'NEGAhi'
    elif i['film'] == 'Pro Neg Std':
        target_tag.find('FilmSimulation').text = 'NEGAStd'
    elif i['film'] == 'Classic Neg':
        target_tag.find('FilmSimulation').text = 'ClassicNEGA'
    elif i['film'] == 'ETERNA/Cinema':
        target_tag.find('FilmSimulation').text = 'Eterna'
    elif i['film'] == 'ETERNA BLEACH BYPASS':
        target_tag.find('FilmSimulation').text = 'BleachBypass'
    elif i['film'] == 'ACROS':
        target_tag.find('FilmSimulation').text = 'Acros'
    elif i['film'] == 'ACROS +Y':
        target_tag.find('FilmSimulation').text = 'AcrosYe'
    elif i['film'] == 'ACROS +R':
        target_tag.find('FilmSimulation').text = 'AcrosR'
    elif i['film'] == 'ACROS +G':
        target_tag.find('FilmSimulation').text = 'AcrosG'
    elif i['film'] == 'MONOCHROME':
        target_tag.find('FilmSimulation').text = 'BW'
    elif i['film'] == 'MONOCHROME +Y':
        target_tag.find('FilmSimulation').text = 'BYe'
    elif i['film'] == 'MONOCHROME +R':
        target_tag.find('FilmSimulation').text = 'BR'
    elif i['film'] == 'MONOCHROME +G':
        target_tag.find('FilmSimulation').text = 'BG'
    elif i['film'] == 'SEPIA':
        target_tag.find('FilmSimulation').text = 'Sepia'

    # Grain
    if i['grain'] == 'OFF':
        target_tag.find('GrainEffect').text = 'OFF'
    if i['grain'] == 'weak':
        target_tag.find('GrainEffect').text = 'WEAK'
    if i['grain'] == 'strong':
        target_tag.find('GrainEffect').text = 'STRONG'
    if i['grain'] == 'weak s':
        target_tag.find('GrainEffect').text = 'WEAK'
        target_tag.find('GrainEffectSize').text = 'SMALL'
    if i['grain'] == 'strong s':
        target_tag.find('GrainEffect').text = 'STRONG'
        target_tag.find('GrainEffectSize').text = 'SMALL'
    if i['grain'] == 'weak l':
        target_tag.find('GrainEffect').text = 'WEAK'
        target_tag.find('GrainEffectSize').text = 'LARGE'
    if i['grain'] == 'strong l':
        target_tag.find('GrainEffect').text = 'STRONG'
        target_tag.find('GrainEffectSize').text = 'LARGE'

    # ColorChromeEffect
    target_tag.find('ChromeEffect').text = str(i['ccfx']).upper()
    target_tag.find('ColorChromeBlue').text = str(i['ccfxb']).upper()
    
    # white balance
    if i['wb'] == 'auto':
        target_tag.find('WhiteBalance').text = 'Auto'
    elif i['wb'] == 'daylight':
        target_tag.find('WhiteBalance').text = 'Daylight'
    elif i['wb'] == 'shade':
        target_tag.find('WhiteBalance').text = 'Shade'
    elif i['wb'] == 'fl light 1':
        target_tag.find('WhiteBalance').text = 'FLight1'
    elif i['wb'] == 'fl light 2':
        target_tag.find('WhiteBalance').text = 'FLight2'
    elif i['wb'] == 'fl light 3':
        target_tag.find('WhiteBalance').text = 'FLight3'
    elif i['wb'] == 'incandescent':
        target_tag.find('WhiteBalance').text = 'Incand'
    elif i['wb'] == 'underwater':
        target_tag.find('WhiteBalance').text = 'UWater'
    else:
        target_tag.find('WhiteBalance').text = 'Temperature'
        target_tag.find('WBColorTemp').text = str(i['wb']).upper()
    target_tag.find('WBShiftR').text = str(i['wbr'])
    target_tag.find('WBShiftB').text = str(i['wbb'])

    # ToneCurve
    target_tag.find('HighlightTone').text = str(i['h-tone'])
    target_tag.find('ShadowTone').text = str(i['s-tone'])
    # Color
    target_tag.find('Color').text = str(i['color'])
    # Sharpness
    target_tag.find('Sharpness').text = str(i['sharp'])
    # NoiseReduction
    target_tag.find('NoisReduction').text = str(i['nr'])
    # Clarity
    target_tag.find('Clarity').text = str(i['clarity'])
    tree = ET.ElementTree(root)

    tree.write('recipe/X-Trans IV/'+i['name']+' by '+i['creator']+'.FP1', pretty_print=True, encoding='utf-8', xml_declaration=True)