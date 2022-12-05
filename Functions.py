from requests import get

def GetUID():
    _NumUid = []
    _AlfUid = []
    #try:
    _ip = get('https://api.ipify.org').text
    _IpLength = len(_ip)
    for i in range(_IpLength):
        _NumUid.append(_ip[i])
    
    for i in _NumUid:
        _AlfUid[i].append(chr(_NumUid[i]))
    _Uid = _NumUid
    return _AlfUid
    #except:
    #print('ERROR: Make shure you are connected to the internet')