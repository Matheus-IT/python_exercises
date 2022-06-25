def mostrar_placa(pl):
    for i in pl:
        print(f' - {i}: {pl[i]}')


placa = dict()
print("\n{:=^44}".format(' DEPARTAMENTO DE TRANSITO '))
carac = str(input('Digite os caracteres da placa: ')).upper().strip()
placa = {'Letras': carac[:3], 'Numeros': int(carac[3:])}
mostrar_placa(placa)

print('A placa digitada e de ', end='')
if ('AAA' < placa['Letras'] < 'BEZ'):
    print('PARANA')
elif ('BFA' < placa['Letras'] < 'GKI'):
    print('SAO PAULO')
elif ('GKJ' < placa['Letras'] < 'HOK'):
    print('MINAS GERAIS') 
elif (('HOL' < placa['Letras'] < 'HQE') or ('NHA' < placa['Letras'] < 'NHT') or ('NMP' < placa['Letras'] < 'NNI') or ('NWS' < placa['Letras'] < 'NXT')):
    print('MARANHAO')
elif (('HTF' < placa['Letras'] < 'HTW') or ('NRF' < placa['Letras'] < 'NSD')):
    print('MATO GROSSO DO SUL')
elif (('HTX' < placa['Letras'] < 'HZA') or ('NQL' < placa['Letras'] < 'NRE') or ('NUM' < placa['Letras'] < 'NVF') or ('OCB' < placa['Letras'] < 'OCT')):
    print('CEARA')
elif (('HZB' < placa['Letras'] < 'IAP') or ('NVG' < placa['Letras'] < 'NVN')):
    print('SERGIPE')
elif ('IAQ' < placa['Letras'] < 'JDO'):
    print('RIO GRANDE DO SUL')
elif ('JDP' < placa['Letras'] < 'JKR'):
    print('DISTRITO FEDERAL')
elif (('JKS' < placa['Letras'] < 'JSZ') or ('NTD' < placa['Letras'] < 'NTW') or ('NYH' < placa['Letras'] < 'NZZ')):
    print('BAHIA')
elif (('JTA' < placa['Letras'] < 'JWE') or ('NSE' < placa['Letras'] < 'NTC') or ('OBE' < placa['Letras'] < 'OCA')):
    print('Para')
elif (('JWF' < placa['Letras'] < 'JXY') or ('NOI' < placa['Letras'] < 'NPB') or ('OAA' < placa['Letras'] < 'OAO')):
    print('AMAZONAS')
elif (('JXZ' < placa['Letras'] < 'KAU') or ('NIY' < placa['Letras'] < 'NJW') or ('NPC' < placa['Letras'] < 'NPQ') or ('NTX' < placa['Letras'] < 'NGU')):
    print('MATO GROSSO')
elif (('KAV' < placa['Letras'] < 'KFC') or ('NFC' < placa['Letras'] < 'NGZ') or ('NJX' < placa['Letras'] < 'NLU') or ('NVO' < placa['Letras'] < 'NWR')):
    print('GOIAS')
elif (('KFD' < placa['Letras'] < 'KWE') or ('NXU' < placa['Letras'] < 'NXW') or ('PEE' < placa['Letras'] < 'PFQ')):
    print('PERNANBUCO')
elif ('KMF' < placa['Letras'] < 'LVE'):
    print('RIO DE JANEIRO')
elif (('LVF' < placa['Letras'] < 'LWQ') or ('NUH' < placa['Letras'] < 'NIX') or ('ODU' < placa['Letras'] < 'OES')):
    print('PIAUI')
elif ('LWR' < placa['Letras'] < 'MMM'):
    print('SANTA CATARINA')
elif (('MMN' < placa['Letras'] < 'MOW') or ('NPR' < placa['Letras'] < 'NQK') or ('OET' < placa['Letras'] < 'OFC')):
    print('PARAIBA')
elif (('MOX' < placa['Letras'] < 'MTZ') or ('OCV' < placa['Letras'] < 'ODT')):
    print('ESPIRITO SANTO')
elif (('MUA' < placa['Letras'] < 'MVK') or ('NLV' < placa['Letras'] < 'NMO')):
    print('ALAGOAS')
elif ('MVL' < placa['Letras'] < 'MXG'):
    print('TOCANTINS')
elif (('MXH' < placa['Letras'] < 'MZM') or ('NNJ' < placa['Letras'] < 'NOH')):
    print('RIO GRANDE DO NORTE')
elif ('MZN' < placa['Letras'] < 'NAG'):
    print('ACRE')
elif (('NAH' < placa['Letras'] < 'NBA') or ('NUH' < placa['Letras'] < 'NUL') or ('NXX' < placa['Letras'] < 'NYG')):
    print('RORAIMA')
elif ('NBB' < placa['Letras'] < 'NEH'):
    print('RONDONIA')
elif ('NEI' < placa['Letras'] < 'NFB'):
    print('AMAPA')
elif (('OFD' < placa['Letras'] < 'PED') or ('PFR' < placa['Letras'] < 'ZZZ')):
    print('INDEFINIDO')
