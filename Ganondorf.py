from logging import DEBUG, basicConfig, exception, info
from os import listdir, getcwd, remove
from random import randint
from subprocess import call
from time import sleep
from matplotlib import pyplot as plt
from numpy import where
from PIL.ImageGrab import grab
from wmi import WMI
from win32con import KEYEVENTF_KEYUP, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_WHEEL, SW_MAXIMIZE
from cv2 import COLOR_BGR2GRAY, IMREAD_GRAYSCALE, NORM_HAMMING, TM_CCOEFF_NORMED, BFMatcher, ORB_create, cvtColor, imread, imwrite, matchTemplate, rectangle
from win32api import SetCursorPos, keybd_event, mouse_event
from win32gui import SetForegroundWindow, ShowWindow, EnumWindows, GetWindowText, GetForegroundWindow













def AsciiArt():
    sleep(5)
    #maximize program
    info("AsciiArt() maximizing window")
    hwnd = GetForegroundWindow()
    ShowWindow(hwnd, SW_MAXIMIZE)
    #print art
    zelda=(
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXKKKKXXXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXK00OOOOOOOO000000KKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kkxxdxxxkkkkkOOOOO000OkxxkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxlclloodddxxkOkOOOOOOOOOOkdlloxOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c;:cllodddxxxxkkkkkOOO00OOkxoc:odoldO0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:,clooooooolloddxkkkkxkkxxxxxdl::c;':c:o0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c;lodkkOxl;;:dO00OkxkOkxxddocclllc,.....:oxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKoclodkkOOOo:cxO0KXNXOkO0kxdxxdolc::;.. ..:cldOXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNxllooddxkxdc;lxKX00XNXOkOOxddddxxdl:,.....',cdkO0KXNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOllllodOKK0kc,,;xXKOO0XKkkOxooodooxxo;......,coddxxxxkO0KKXXNNWNNNXXXXKKKKKKKKXXXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxclodxk0XNKd;,,,cO0kddkOkxkxolcoo:;llc;..'',;;;;cllodddddxxkkOOOkkkkkxxdxxxxxxxxxkO0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMW0lcodxxkKXNO::cloldOkocoddxxkdcccdxc,::;,,''''.,:odxkkkkkxxxxxxkkkxxddddxxkkOOkxxxxkxxkkO0KXNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXOl:llldxkO0XkclxkOxdkkd::llodxdcclcoxc;:;''''.',;cldxxkkkkkkkkkxxxxdddddxxkkkkkxddddddddxxxxkkO0KXXXNNWWWMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKdc:;:::ooxolkxloOKXXOdxdl;;::cool:lo::dc;;;'.',',;:clloddddddxxddddddddooooooooll::::ccccllloooddxxxxxkkOO0NMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOo;',,;clol;cdcckXNWXxlolc:;;::cc::l:',c:;,'..',;;,',;:coddddddddoollc:;;,,,''''..'',;::ccclllllloooddxxkk0NMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXx:''.'cccc::cc:cxXWWKdlllc::;;;:;;:;'..',,'...';:;,,;:cllllllcc:;,'....',:cllooodddddxxxxkkkOO0KKXXNNWWMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXl',..:l::cllc::coOXWXdlooccc:;;;,,,'.........';::;;;;;;;;,,,'...';ldk0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxxXWMMMMMNkxl'.;ol:cdxdc;cccoOKKxdxolol:;,'''.........',,,,,''''......;cdOKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:,cdONXKKKKNO:',colcdO0OxkKOddk0Kkxoc;'.':,','..'.''.  .'coddolloodxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxoc:;;:;...'ok:.,;clox0NNNNNNXKKKXOocc;;:ooc;,,':dlokkdlccxKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNWWWMMMMMMMMMMWKxdoc;,'.. ...','..;:cldOXNWWWWWNXXXklxOkxxxoc,...lXWXXWMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOOXNXXXNNWWMMMMMMMXxdoc;'........,c:..;:;:cdKNWWWWWNXXKxldO0OOkd:....:KWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xoxKOkOOKK00KNWWMMNklooc;'.''....;xd:,',:;,cxOKNNWWNXKXKdldkOOkdc'.....:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkdodd0NKOddOkxxxO0KNNKxooodoolllcc::ldlcc:',;',oO0KXXNNX0Oxoddxxdo;. ......'lONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMWKxlooookXNOxddxkO0kddxKXXXK0Okkxkkxxxxddolccc:';,.,lk0KKKK0Okxddddoc'   ......',:oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMWKxoooolclkNN0xdkKXNKdclk0KKXXNNXXK0Okkxxxxxdoccl:,,'.':d0XXXK0Okxdoc,...  .......,;:lxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMWKklcoxkxlclkXKkddkOkxo:.';coxOKKXKXXXXK00Okxddol:cl:'...';lx0XXK0xoc:'.','.. ......';;cllxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMNKOkxl:lddolookKOkkxdloo;,,;;;,,;:cldkOO000KKK0OOxoccll:,,;::::cllllc:;,.';;;,'........,;::;:oxO00XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMWNKOkkxc,.,ooldxkKWMMWXxoc;;cllllccc;,'',;cldkO0KKKK0kkkkxdloddddl:;;;;;;'.',;::;,. .'....',,',;;;:clclxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMWXKOkxo:'.',,:ooxkkOKWN0kd:,;cllooolllcc:::,'',;:d0K00OO0KKXNNkooldkdc,'''..'',;::;,...,'....''.',,;;;::,;dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMWNK0Okd:,..,;;;;;:ccodxKXx;,;:clcclodolllllcccc:c:::okkoooxKNWMMWOl;,oOkxl::;,::;;clcc:,..;;'',,'...',;;',;,'cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMWXKOkdl;..',;;;;;;;,'.;d0Ol,;cllllllloooolclooolcccccloo;,lodXMMMMWkl:;xOOkxdollc::ldool;'..:;'':,...''';,'...,lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMWNK0kxo:'.';;;:cc:;:::;;,,o0d,,cooooolllloooolc::oddlc:cclddlod0WMMMMNkl::kK0OxdddoodkOkdl:''.';;.';'....',;,'..';oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMWXK0OOxc,..,;::cllc:::codllccd0d,;ool:;lxdoloolllccccldxoc::cdXWWWNXWMMMXdcc:ldxxkkOOkkkxdl:;,'..,;,..;'....,;;,..',..,lkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MWNK00OkOOkl..,;;;cooc;:c:lkxc;;;lx0o';lool:ckxocloooloooolcoxolcccool:,lXMMMXoll:::::clllccc::;;,''.''..';;...',,,'..',.     .:d0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "K0OOkxdoxkxo,.,;:dkd:;;::;x0l,;:codxkl;:llc:oxoc:lodddddddol:ldxolll:;;;dNMMMKlcc:::::,,;::::;:;,'.......lOl,..',''.'',;'..      .:xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "Oxkkddxccdl,.',ckko:;:::;;d0o;;cdddddxd::cl:clddlllloooooddoc;cxkdlloollOWMMM0lc:,;ccc:;;:::::;;,........cOc,.........';;;,,......  'lkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "Kxxkoc::cc,.',lOkc;;::c::ckOd::oddddxddxo:clc:cdkxoodxxxddolc:,:xkdoloodKMMMWOcc;,';::cc:::::;;;,.....'..ok,........ ....',;,,:ll:;;'..'cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "Nkoxxdooo;'',l00l;::::::okxl;:lc;;,,;;;okxl:llc:okkkOOOOOOxlcccldxxdlodxXMMMNxcc:;,,;:::cc::;;;,.....''.;Ol........  .....',;cllc:oxxo:,. .:d0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "M0ooo;','.''c0Kd;,;;:;:oxxl;:ooc...',:dOOOOdccoolooloooodkOkkkxdoooolodkXMMMXd:::::;;:cc:::;;;,'....,,..;:........  ....'';ldodoccooodxxo:'. .;coOXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MXdoo' ..'';kKk:',:looxxdc;cooddo,.,lxO000kkxooloooooolllokOxxddoddddxxONMMMKl::::c::::lc:::;;,....,;....,.......  ....',;colccc:clooooooddoc'.....;cdkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MNkod:..'''o0kc',okxdlclc;clooooolcldddddoolldkddxooxxxxxdxkddxxxxxxkxd0WMMMOc:;:::ccc::c:::::;...',....xXkl:'......''',;,,;;;:;:ldolllddolll:,;:;'.......';cxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MW0ddl...''lxoooOKkdc;,;:llc::::::::ccccccccccloooldxkkkkkkkOkkkxxdxkxxXMMMNd;;;;:::ccccc:;;;:;........lNMMWNKd'.....',;'.',,..;::::clollc::cclllc;col:,''...,0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMXkdo;...';:cloO0d:;;:clc,'',,;;;:clloododdxxxdddxkkkOOkkkkkkkkxxxkOxONMMMXo;;,,;::::cclcc:::;.......'kWMMMMMO,.....',...,,..',,;:::::;,;;:c:cllcclooooodxd:dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMWOooc'..'',,,;:c;,;;;;;',;:c::ccccllloddddxxkkkkOkkkkkkkxxxxxxxkkOkx0WMMMO:;,'';;:ccccccc:;,.. ... .cXMMMMMMWX0kol::;......',::::;;,'',,.',,;;;;;cooddddl:;lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMM0ool,..',,,''',,;;;;,,;;;:::cccccllllodxxxxxkkxxxkkkkkOOOkkkkOOOkkkKWMMNd;;'.'',;:::::;,'....... ..xWMMMMMMMMMMMWWWN0kdllcc:;,,''..'''......'',;cclool:;;;;;o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMXxoo;..''''',,,,,,;;;;;;;;:cc::clllllodxxxkxxxxkkkkOOOOkkkkxkOOOOkOXMMMKl;;'..''',,'''............'dWMMMMMMMMMMMMMMMMMMMMWNXK00kxdoc'.........,;;::,....;cc;,:xNMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMWOoo:...'''''',,,,,,;,,;;;::::cccllllodxxxxdxkkkkkkkkkxxxxkkkOOOkkKWMMWk:;,..''''''................oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,''...',,'''..    .,clc:;,l0WMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMKdlc,..'''',,,,,,;;;;,,;;;;::ccccllodddxxdxxxxkkkOOkkkkkOOOOOOkx0NMMMKl,,.........  ..............:KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxxkko;'.... .. .. .:ool:,,:xXWMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMNklc;...'''',,,,,,;;;,;;;;;::ccccclooddddddxxkkOOO00OOOOOOOkkkxkXWMMWx;''.....................'...':dxkkOOKWMMWNX0kdododxKWMMMMMMMMMMMMMMWXKOd:';dc;:;'.;odocldc:lxO0Okx0WMMMMMMMMMMMMMMMM",
        "MMMMMKocc,....'''',,,,,,;;;;;;;;::::ccllooddddxxxxxxkkkkkkkkkxdddox0NWMW0c''.......''.........,::cc'...',;:;;,:xOkdo;,;cc,...'cONMMMMMMMMMMMMMMMMMN0KKkO0xl:,lddc'',,;:::;,'dNMMMMMMMMMMMMMMMM",
        "MMMMMNkll:'..'''',,,,,,,,,;;;;;::::cccclooodxxxkkxxxxkkkkkkOOOOkdox0XWWNo''.......''........';::,.........',,;cllc:;:oooodxkOOOKNWWWWWWWWMMMMMMMMMMXkclKX00x:;lo:..'.',,,;,:OWMMMMMMMMMMMMMMMM",
        "MMMMMMKdll:...''''',,,,,,,,;;;;;:::ccccllodxddddxxkkkkkkkkO0KXNXXK0KXNNx,'.................',........   ...';:ccc;';oxxKNNNNNNNNNNNNWWWWWWWMMWWWWMMNx'.:ccxOllOKd:do..'''.;kWMMMMMMMMMMMMMMMMM",
        "MMMMMMWOool;...','''''',,,,,,,;;;;:::ccllodxxdddddxxxxxxxkOKWWWWWNNNNNk;'...................'..'.....   .',,:ccc:';ldO0KKKXXXXXKXXXXXNNNWWWWWWWWWWWWXOd:...''lKNOool;,'''',cxKWWMMMMMMMMMMMMMM",
        "MMMMMMMXxodl,.':c:,''',,,,,,,,,,;;;::cclloodxxxxddddddddddxKWWWWWNXNNO;......................'....   ...',,:cclc,.cdx0KKKKKKKKKKKKKKKXNNNNWWWNNNNNNNNNWNOkdc:oOklc::c:,'.';:o0NWWMMMMMMMMMMMMM",
        "MMMMMMMMKxddlcoddoc,'''',,,,,',,,,;;::cclloooodoooooooooollxXNNNNWNNO:.................................';;;clll;',cdO00000OO00K0OO0KXXNNNNNNNXXXXXXXKKNMMMMWN0xl:::;;,',;llcok0KXNWWWMMMMMMMMM",
        "MMMMMMMMWKxxxxkOkxoc,.',,,''''',,,,;:::cllllllolccllloolll::xKXXNNNk;............................'...',::;:looc'.cxxkOOkkkOOOOxxO0KKKKXXXNNXXKKKKKKKK0KWMMMMMWNKOOkxxko;:clc;:lodOKXNWWWMMMMMM",
        "MMMMMMMMMW0xdkkkkkd:..',,''''',,,,,;;;::ccclllccccccllccc:clxKNNNXx,......................''',,,'..',,:c;;llol,';cddoddxxkOOxdxk0OOOKKKKKKXXK000000KKO0NMMMMMMMMMMMMMMNx,..''''',:ok0KKKKXXWMM",
        "MMMMMMMMMMWKxoxkkxd;..',c:'''',,,,,;;;::::::::ccc::ll:::;cxOKNWNXd,....................';;;;;;;,'',;;:l:;:lll;.:l:lolodxkOkddkOkdook000000000O0000000kkNMMMMMMMMMMMMMMMWKl',::;'''',:llllclxKN",
        "MMMMMMMMMMMMXxoxkxo;..'';dl,'''',::;,;;;::col:;;:clc;;;;cd0NWWWKl'....................',;::;;::,,;ccclc;:cloc'.cl:;codxkxddxkOko:lxkkkkOOkkkkkOOOOkxdlkWMMMMMMMMMMMMMMMMMNOlokl'',:ol;'',,,;:d",
        "MMMMMMMMMMMMMNkodkxo:,..';odc,.,c::;,;;;;,,;lolcoo:,,,:ld0WWWW0:....................',,;;::ccc:;:lllol::clol,.;l:;cldxxdodxkkxc;cdxxxkkkxdddxxxddolc;;dNMMMMMMMMMMMMMMMMMMMNkl;;,',oXXOd:'',,:",
        "MMMMMMMMMMMMMWKdodxxdo:'..':odccc,'',,,;:;;;;cddc;,,,:oOKWWWNx,...................',,;;::clll::clllooc::lol;',::,;ccllldkO0Oxc';lddxkkxddddddolllc;',:cOWMMMMMMMMMMMMMMMMMMMMNkl;,'cKMMMNOo:,,",
        "MMMMMMMMMMMMWXxc:codkxol;'...;clc,';;:loxxl,,,;;;,;:lxKNWWWKl'..................'',,;;:clllc:clllllolcccll:',cccc,,ccldkOkkd:..:looollodxxdolc:::;,,,''dNMMMMMMMMMMMMMMMMMMMMMMN0kk0WMMMMMWXOd",
        "MMMMMMMMMMMWXkl;'.,lddxxdl;'...',',cc:lx0XKd;',,,:xO0NWWWXx;...................'',,,,;:cllcclllcclollcloo:.,cl;,:'';cldxxo:'..''';coodddddllc:;,,,'..',dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMWXkl:,',::;codkkdl:,'...;lc;:oONWNO:';d0XWWWWNOl,........................',;::::cllcccloolcloo:'';cl:;'';coddo:,....,;,,;;:cccl:'''''',,;;;''xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMNOoc:',cc'.,oooxkxdlc;''coc,:olOWMMKO0XWMMWN0o;'..  ....................',,;;::lllcclooolclllc'':l:::'.';clc;'........,;::cclcclllooool:;'..:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMNOolc,,c:..,xNXOxdodxdooooo:;d0ooNMMMMWMMWWKd:'...    ..'...............',,;::cccc:ccooollllc:'':loc;,...'''.',;cc'.......',;::cccc:,'......'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMN0dlc,.;:,',xNMMMWKkoodxxxxxo::okXWMMMMMMWXx:'':::;:cldo,..........'....',;;:cclc::clooollllc;..cllodl:cclodxk0XNW0,.........'''''''........,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMW0dl:'.,;,';xNMMMMMMWXOdlldxxkxoOWMMMMMMWKx:'':xNWWWMMMMNd'...........''',,:cclllccllooolllcc,.,:lx0NNWWWWMMMMMMMMMO' ......................'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMWKdl:,',;'.:kWMMMMMMMMMMWKkdoodddkNMMWMW0d:'':xXMMMMMMMMMMNo............'';:clloolllodoollll:'.,clkXNWMMMMMMMMMMMMMMO' ...''''...............cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMWXkl:,,;,..lKWMMMMMMMMMMMMMWNKkxoldKWNXkl,.':kXMMMMMMMMMMMMMXl..........',:clloooooolooooolc;..:lloONWMMMMMMMMMMMMMMMX:......',;,,,,'''''....'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMXkoc;,;,';dXMMMMMMMMMMMMMMMMMMMNKOk00d:'.'ckNMMMMMMMMMMMMMMMMXl.......,;::cloddddooollolll:'.,cololoKMMMMMMMMMMMMMMMMWx........''''''........cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMW0oc:::;,:kNMMMMMMMMMMMMMMMMMMMMMMMWXx;.'cONMMMMMMMMMMMMMMMMMMMXc.....',:cclloodddooolllc:,';::looollkWMMMMMMMMMMMMMMMMXc.........''.........'kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMKdc::::;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMN0KWMMMMMMMMMMMMMMMMMMMMMWx......,;:clooddooloolc:,'':;:lcllloddKMMMMMMMMMMMMMMMMMk'........''.........cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMNxc;::;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:....'';:loooooollll:,',:cc:okkddokOxOWMMMMMMMMMMMMMMMMNc........''........'kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMM0c,,,;oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk,.',,;:clloooolc:;;:;:lldoldk0OxokKkkNMMMMMMMMMMMMMMMMMk'......'''........cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMWk:''c0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,',;;:cclllc:;,,;ccc:cdkkx0XXKOdxKOd0WMMMMMMMMMMMMMMMMX:......'''......':kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMW0ooONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;,,;::::;,,';::cclxkxkOO0XNXX0koOKxkNMMMMMMMMMMMMMMMMNc......'''......:kXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxc'''',;::;llllcok0KXXKKXNNXKOdxKOdKWMMMMMMMMMMMMMMWO,...............dNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdc:coc:cc;:ldkOKXXXXXXXNNXK0xd0KxkNMMMMMMMMMMMMMMO,......'........'kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kddOxl::cccdO0KKKXNXXXNNXK0Ox0XOxXWMMMMMMMMMMMMNo.......'''.......xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXNXKl;::ldkO0K0XNNNNNNNXK0k0NKxONMMMMMMMMMMNx:'.......''''.....'xWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd::lodk000KNNNNNNNXXKO0XXkxKWMMMMMMMMXo'.......',,,;,,,,''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc:llxOOO0XNNNNNNXXK00XNOxONMMMMMMW0c'''......',,;;;;;,'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc:lokOkkKXNNNNXXXK00XNKkkKWMMMMMXl..........',;;;,,,';OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0lclxkxx0XXNNNXXXKK0KNXOk0NMMMMMNo............''''...;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdcokkxOKXNNXXXXXKKKXNK0OKWMMMMMKc............',,,,,,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOlokxx0KXNNNNNXXKXXNNKOONMMMMMMXd,..........',,,,'.cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxdddkKXXNNNNNNXXXNXX0xxOXWMMMMW0c........',,,,,;,,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdodOKXXNNNNNNNXXXXKOoccd0WMMMMNd'......,;;;;::,'cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0oldO0KXXNNNNNXXXXKOkdc,;xXMMMMWO,.....',;:;;,,',o0XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0oldO0KXXNNNXXXKK0Okxx:',l0WMMMWk,....',;;,,,,,,,;oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXdldkO0KXXXXKK0OOkkO0o'',:kWMMMWd....',;;,,,,,,,,,oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo;ldxO00000OOkkkkO0x,.,,,xWMMMK:...',;:;;,,,,;;,,dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl';:codddxxxxxkkO0Oo'.,:',0MMMWx'.'';::::;;,,;;;,:0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo,,;clllooddxxkxxdl,.'cc'.oNMMM0;.',;::::;;;;;;:;;kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd;'':lloddoooool:,..'ld;..,kWMMNo..',;::::::c:::c:oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc,'';cccc::::;,..':od:''..;kWMMNd,..';:clollllllcc0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c''''.........,cddl;,'...,:kWMMWKl'..';coddollllckWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:',,''''',;clooc;,,'...,;';0MMMMWKo,..,:loddoc;lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKc.',,;;;:;;,'.',,'...;:,..cXMMMMMMXkc,'';::;:dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,.........''''...,::,'..'xWMMMMMMMWX0kkkO0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo'...........',;;,'.....:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;..''''''',,,'........'dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo'.'',,,'''......''''.;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOc....''''''''''',,,''cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk:..''',,',,''',,,,',dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,..',,,,,,,,,,,,,',dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c'.',,,,,,,,,,,,,',oKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk:.'',,,,,,,,,,,,,;cxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd,',,,,,,,,,,,;;;;cdkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c,,,,,,;;;;;;::cccodOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl',,,;;;;;::coo:;lllONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXl',;:::::loxdc:cc:;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkc;:cccllllccll;.''cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo'';;;;;:cc:,'...,oOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;',,;;,,'','....,;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0c..''',,,'...'',,;lkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;.''''.',;,,;;;;:lxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKl'.',,,;:::::::ccldONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,.'',,;;::clloolodkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;.',;;:looooddddoookXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0;.,:clloooodxxxxdollOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0;.,:clloddxk0KK0ko:cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.;:ldxkkO0KXXXKko:lKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0;':lxO000KXXXXK0xlckWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;':okO0KKKKKK00OdcoKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l,;lodO000000KOoc:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOl;',cdO000kdc;,,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkd:,:lll:;,':kNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkl:,;;:lkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
        "GANONDORF: because who wants to duel link these days?\nCreated by 0rphon\n\n")
    for x in zelda:
        print(x)
        sleep(0.015)



#check if duel linsk is running
def CheckIfRunning():
    c = WMI ()
    #iterate through running processes
    for process in c.Win32_Process ():
        #if process named dlpc.exe is running
        if process.Name=="dlpc.exe":
            return True
    #if no process that matches name
    return False


#focus on duel links
def Focus(window):

    def windowEnumerationHandler(hwnd, top_windows):
        top_windows.append((hwnd, GetWindowText(hwnd)))

    top_windows = []
    info("Focus() scanning active windows")
    EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if window in i[1].lower():
            info("Focus() valid window found. focusing on window")
            ShowWindow(i[0],5)
            SetForegroundWindow(i[0])
            return
    info("Focus() no valid window found")



#launch duel links from start menu shortcut
def Start():
    #if duellinks not running launch
    info("Start() checking if duel links running")
    if CheckIfRunning()==False:
        info("Start() no process found. launching duel links")
        keybd_event(0x5B,0,0,0)    #win
        sleep(0.1)
        keybd_event(0x5B,0,KEYEVENTF_KEYUP,0) #win up
        sleep(3)
        keybd_event(0x44,0,0,0)    #d
        sleep(0.1)
        keybd_event(0x55,0,0,0)    #u
        sleep(0.1)
        keybd_event(0x45,0,0,0)    #e
        sleep(0.1)
        keybd_event(0x4C,0,0,0)    #l
        sleep(0.1)
        keybd_event(0x20,0,0,0)    # 
        sleep(0.1)
        keybd_event(0x4C,0,0,0)    #l
        sleep(0.1)
        keybd_event(0x49,0,0,0)    #i
        sleep(0.1)
        keybd_event(0x4E,0,0,0)    #n
        sleep(0.1)
        keybd_event(0x4B,0,0,0)    #k
        sleep(0.1)
        keybd_event(0x53,0,0,0)    #s
        sleep(0.1)
        keybd_event(0x0D,0,0,0)    #enter
        sleep(0.1)
        keybd_event(0x0D,0,KEYEVENTF_KEYUP,0) #enter up
        sleep(20)
    #if duel links running kill duel links
    else:
        info("Start() process found. restarting")
        Restart()



#sleep for 5-15 minutes then relaunch duel links
def Restart():
    #if duel links running
    info("Restart() checking if duel links running")
    if CheckIfRunning()==True:
        info("Restart() process running. focusing on duel links window")
        Focus("duel links")
        info("Restart() closing duel links and sleeping")
        keybd_event(0x12,0,0,0)    #alt
        keybd_event(0x73,0,0,0)    #f4
        sleep(0.1)
        keybd_event(0x12,0,KEYEVENTF_KEYUP,0) #alt up
        keybd_event(0x73,0,KEYEVENTF_KEYUP,0) #f4
        #sleep for between 5 and 15 minutes
        sleeptime=randint(300,900)
        info("Restart() sleeping for "+str(sleeptime)+"seconds")
        sleep(sleeptime)
        info("Restart() starting duel links")
        Start()
    #if not running
    else:
        info("Restart() no process found. starting duel links")
        Start()






#take screenshot
def Screenshot():
    # grab fullscreen
    info("Screenshot() taking screenshot")
    im = grab()
    # save image file
    info("Screenshot() saving screenshot")
    im.save('screen.png')



def SeekDuelist():
    for times in range(4):
        info("SeekDuelist() getting screenshot")
        #get screen image
        Screenshot()
        #iterate through sprites
        info("SeekDuelist() iterating through duelists")
        for image in listdir("TEMPLATES\\characters\\"):
            #set sprite
            pic="TEMPLATES\\characters\\"+image
            #read sprite image
            img1= imread(pic,IMREAD_GRAYSCALE)
            #read screen image
            img2= imread("screen.png",IMREAD_GRAYSCALE)

            #set ORB object
            orb= ORB_create(100000)

            #feature detect sprite
            kp1, des1= orb.detectAndCompute(img1, None)
            #feature detect screen
            kp2, des2= orb.detectAndCompute(img2, None)

            #match features from sprite and screen
            bf = BFMatcher(NORM_HAMMING, crossCheck=True)
            matches = bf.match(des1, des2)
            #sort accuracy of matches
            matches = sorted(matches,key=lambda image:image.distance)

            #select accurate matches
            found=[]
            for m in matches:
                if m.distance<=20:
                    found.append(m.distance)

            #check if accurate matches were found
            if len(found)!=0:

                #set image info
                img2_idx = matches[0].trainIdx
                
                # Get the coordinates
                # x - left to right
                # y - top to bottom
                (x,y) = kp2[img2_idx].pt
                info("SeekDuelist() match found for "+image+" at ("+str(int(x))+", "+str(int(y))+")")
                return (int(x),int(y))
        #Scroll one down to change screens
        info("SeekDuelist() no matches found. scrolling")
        mouse_event(MOUSEEVENTF_WHEEL, 0, 0, -1, 0)
        sleep(2)
    info("SeekDuelist() no matches found. raising exception")
    raise Exception






class Icon():
    autoduel="autoduel.png"
    okay="ok.png"
    close="close.png"
    no="no.png"
    nxt="next.png"
    link="link.png"
    back="back.png"
    chat="chat.png"
    toolbar="toolbar.png"
    cancel="cancel.png"
    reboot="reboot.png"
    duelorb="duelorb.png"
    vegabond="vegabond.png"


#test scan for icon
def Scan(icon,threshold=0.8):
    #get screenshot
    info("Scan() getting screenshot")
    Screenshot()
    #read screenshot
    img_rgb = imread('screen.png')
    #convert to grey
    img_gray = cvtColor(img_rgb, COLOR_BGR2GRAY)
    #read template
    info("Scan() scanning for "+icon)
    template = imread('TEMPLATES/'+icon,0)
    #get dimensions of screen
    w, h = template.shape[::-1]
    #scan screen for template
    res = matchTemplate(img_gray,template,TM_CCOEFF_NORMED)
    #get location of match
    loc = where( res >= threshold)
    #get coordinates
    for pt in zip(*loc[::-1]):
        rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        imwrite("res.png",img_rgb)
        cords=pt[0]+(w//2),(pt[1]+(h//2))
        #return coordinates
        info("Scan() valid template found")
        return cords
    #return false if nothing found
    info("Scan() no valid template found")
    return False
    #first number is horizontal left to right
    #second number is vertical from top to bottom
    #exports upper left corner



#click mouse at coordinates
def Click(cords,times):
    for click in range(times):
        info("Click() clicking")
        x=cords[0]
        y=cords[1]
        SetCursorPos((x,y))
        mouse_event(MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        mouse_event(MOUSEEVENTF_LEFTUP,x,y,0,0)
        sleep(5)






#login to portal
def Login():
    info("Login() scanning for link.png")
    coordinates=Scan(Icon.link)
    info("Login() clicking "+str(coordinates))
    Click(coordinates,1)
    info("Login() clicking through rewards screen")
    RewardScreen()



#click icon until you dont see icon
def ClickThrough(icon):
    while True:
        sleep(10)
        #check to see if icon on screen
        coordinates=Scan(icon)
        #if icon on screen
        if coordinates!=False:
            #click icon
            Click(coordinates,1)
        else: break



#wait to click icon until you see the icon
def WaitTil(icon):
    while True:
        #get screen
        info("WaitTil() getting screenshot")
        Screenshot()
        #check to see if icon exists
        info("WaitTil() scanning for "+icon)
        coordinates=Scan(icon)
        #if icon exists
        if coordinates!=False:                   
            #click icon
            info("WaitTil() found icon. clicking "+str(coordinates)) 
            Click(coordinates,1)
            #exit loop
            return
        info("WaitTil() scanning for reboot.png")
        if Scan(Icon.reboot)!=False:
            info("WaitTil() reboot.png found. raising exception")
            raise Exception
        sleep(5)



#click until you see icon
def ClickTil(icon):
    for x in range(5):
        #click
        info("ClickTil() clicking")
        mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
        #get screen
        info("ClickTil() getting screen")
        Screenshot()
        #check to see if icon exists
        info("ClickTil() scanning for "+icon)
        #if icon exists        
        if Scan(icon)!=False:                    
            #return
            info("ClickTil() icon found")
            return
        sleep(5)
    info("ClickTil() clicked more than 5 times. raising exception")
    raise Exception



def RewardScreen():
    def ClickIcon(icon):
        #if icon on screen
        info("ClickIcon() Scanning for "+icon)
        coordinates=Scan(icon)
        if coordinates!=False:
            info("ClickIcon() found "+icon+" clicking "+str(coordinates))
            #click icon
            Click(coordinates,1)
            return True
        #if no icon
        info("ClickIcon() "+icon+" not found")
        return False


    while True:
        sleep(10)
        #check to see if any icon on screen
        info("RewardScreen() scanning for next.png, okay.png, close.png, back.png, no.png, and cancel.png")
        if (ClickIcon(Icon.nxt)==False and ClickIcon(Icon.okay)==False and
            ClickIcon(Icon.close)==False and ClickIcon(Icon.back)==False and
            ClickIcon(Icon.no)==False and ClickIcon(Icon.cancel)==False and
            ClickIcon(Icon.vegabond)==False and ClickIcon(Icon.duelorb)==False): 
                info("RewardScreen() found no matching images")
                return
        #check if duel orb prompt on screen
        info("RewardScreen() checking for duelorb.png")
        if Scan(Icon.duelorb)!=False:
            #sleep then raise exception
            info("RewardScreen() found duelorb.png. sleeping 15 minutes then raising exception")
            sleep(900)
            raise Exception






def Main():
    print("starting")
    info("\n\nMain() Starting")
    Start()
    while True:
        try:
            print("logging in")
            info("\n\nMain() logging in")
            Login()
            
            while True:

                print("finding duelist")
                #find duelist on screen
                info("\n\nMain() seeking duelist")
                coordinates=SeekDuelist()

                print("clicking duelist")            
                #click at duelist then click through speech
                info("\n\nMain() clicking "+str(coordinates))
                Click(coordinates,1)

                print("clicking through chat")
                #keep clicking til chat icon is gone
                info("\n\nMain() clicking through chat")
                ClickTil(Icon.autoduel)


                print("finding autoduel icon")
                #find auto duel icon
                info("\n\nMain() finding autoduel.png")
                coordinates=Scan(Icon.autoduel)

                print("clicking autoduel icon")
                #click auto duel icon
                info("\n\nMain() clicking "+str(coordinates))
                Click(coordinates,1)

                print("waiting for duel")
                #wait to click til you see okay
                info("\n\nMain() waiting for duel")
                WaitTil(Icon.okay)

                print("clicking through rewards screen")
                #click through rewards screen
                info("\n\nMain() clicking through rewards screen")
                RewardScreen()

                print("Clicking through chat")
                #keep clicking til chat icon is gone
                info("\n\nMain() clicking until toolbar.png")
                ClickTil(Icon.toolbar)

        except Exception:
            print("restarting app and sleeping for 5-15 minutes")
            exception("\n\nMain() ERROR: ")
            info("\n\nMain() exception raised. restarting")            
            Restart()







if __name__=="__main__":
    call("cls",shell=True)
    #attempt to remove old log
    try:
        remove(getcwd()+"\\Ganondorf.log")
    except:pass
    #create new log
    basicConfig(level=20, filename='Ganondorf.log')
    info("PRINTING ART")
    AsciiArt()
    print("loading")
    sleep(10)
    #launch main    
    while True:
        info("STARTING MAIN FUNCION")
        try:
            Main()
        except KeyboardInterrupt:
            info("\n\n\nKEYBOARD INTERRUPT EXITING")
            exit()
        except:
            info("\n\n\nMAIN FUNCTION CRASHED")
            exception("MainfuncionERROR: ")