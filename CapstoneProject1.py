# Capstone Project Module 1 (Gudang - Data Stock)

ListItem = [
    {
        'ID' : '00001',
        'NamaProduk' : 'Teh Botol 200 ml',
        'Stock' : 20,
        'Harga' : 5000,
        'Locator' : 'A.001'
    },
    {
        'ID' : '00002',
        'NamaProduk' : 'Extra Joss Original',
        'Stock' : 100,
        'Harga' : 1500,
        'Locator' : 'A.002'
    },
    {
        'ID' : '00003',
        'NamaProduk' : 'Extra Joss Anggur',
        'Stock' : 100,
        'Harga' : 1500,
        'Locator' : 'A.003'
    }
]

def PrintMenu():
    print('Selamat Datang pada Inventory Management System: ')
    print('------------------------------------------------ ')
    print('1. Menampilkan Item di dalam sistem.')
    print('2. Menambah Item di dalam sistem.')
    print('3. Menghapus Item di dalam sistem.')
    print('4. Update Item di dalam sistem.')
    print('5. Keluar Menu.')

def PrintMenuUpdate():
    print('1. Update Nama Produk.')
    print('2. Update Stock Produk.')
    print('3. Update Harga Produk.')
    print('4. Update Locator Produk.')
    print('5. Exit to Main Menu.')

def PrintMenuShowItem():
    print('1. Menampilkan Semua Item.')
    print('2. Menampilkan Item tertentu.')
    print('3. Exit to Main Menu.')


def PrintItem(ColItem):
    print('ID\t|Nama Produk\t\t|Stock\t|Harga\t|Locator\t|On Hand Value')
    for x in ColItem:
        print('{}\t|{}\t|{}\t|{}\t|{}\t\t|{}'.format(x['ID'],x['NamaProduk'],x['Stock'],x['Harga'],x['Locator'],x['Stock']*x['Harga']))

def PrintSpecificItem(ColItem, ItemID):
    idx = 0
    for x in ColItem:
        if(x['ID'] == ItemID):
            break
        idx += 1
    if(idx == len(ColItem)):
        print('Item dengan ID {} tidak ditemukan'.format(ItemID))
    else:
        print('ID\t|Nama Produk\t\t|Stock\t|Harga\t|Locator\t|On Hand Value')
        print('{}\t|{}\t|{}\t|{}\t|{}\t\t|{}'.format(ColItem[idx]['ID'],ColItem[idx]['NamaProduk'],ColItem[idx]['Stock'],ColItem[idx]['Harga'],ColItem[idx]['Locator'],ColItem[idx]['Stock']*ColItem[idx]['Harga']))

def AddItem():
    while(True):
        InputID = input('Masukkan ID produk (5 Karakter): ')
        FlagDuplicate = False

        if(len(InputID) == 5):
            for x in ListItem:
                if(x['ID'] == InputID):
                    print('ID sudah ada.')
                    FlagDuplicate = True
                    break
            
            if(FlagDuplicate == False):
                break
        else:
            print('ID Produk harus 5 karakter.')
                    
    InputNamaProduk = input('Masukkan Nama Produk: ')
    InputStock = int(input('Masukkan Stock Produk: '))
    InputHarga = int(input('Masukkan Harga Produk: '))
    InputLocator = input('Masukkan Locator Produk: ') 

    ListItem.append({
        'ID':InputID,
        'NamaProduk':InputNamaProduk,
        'Stock':InputStock,
        'Harga':InputHarga,
        'Locator':InputLocator
    })
    PrintItem(ListItem)

def DeleteItem(ColItem, ItemID):
    idx = 0
    for x in ColItem:
        if(x['ID'] == ItemID):
            break
        else:
            idx += 1
    if(idx == len(ColItem)):
        print('ID {} tidak ditemukan di dalam sistem.'.format(ItemID))   
    else:
        del ListItem[idx]
        print('Item dengan ID {} telah dihapus'.format(ItemID))
        PrintItem(ListItem)     

def UpdateItem():
    InputID = input('Masukkan ID produk (5 Karakter): ')
    idx = 0
    for x in ListItem:
        if(x['ID'] == InputID):
            break
        idx += 1
    if(idx == len(ListItem)):
        print('ID {} tidak ditemukan di dalam sistem.'.format(InputID))   
    else:
        while(True):
            PrintMenuUpdate() 
            InputMenuUpdate = int(input('Masukkan menu yang ingin dipilih: '))

            if(InputMenuUpdate == 1):
                InputUpdateNamaProduk = input('Masukkan Nama Produk baru: ')
                ListItem[idx]['NamaProduk'] = InputUpdateNamaProduk
            elif(InputMenuUpdate == 2):
                InputUpdateStock = int(input('Masukkan Stock Produk baru: '))
                ListItem[idx]['Stock'] = InputUpdateStock
            elif(InputMenuUpdate == 3):
                InputUpdateHarga = int(input('Masukkan Harga Produk baru: '))
                ListItem[idx]['Harga'] = InputUpdateHarga
            elif(InputMenuUpdate == 4):
                InputUpdateLocator = input('Masukkan Locator Produk baru: ')
                ListItem[idx]['Locator'] = InputUpdateLocator
            elif(InputMenuUpdate == 5):
                break



while(True):
    PrintItem(ListItem)
    PrintMenu()
    InputMenu = int(input('Masukkan menu yang ingin dipilih: '))
    if(InputMenu == 1):
        while(True):
            PrintMenuShowItem()
            InputShowItem = int(input('Masukkan menu yang ingin dipilih: '))
            
            if(InputShowItem == 1):
                PrintItem(ListItem)
            elif(InputShowItem == 2):
                SearchItemID = input('Masukkan ID Item yang ingin ditampilkan: ')
                PrintSpecificItem(ListItem,SearchItemID)
            elif(InputShowItem == 3):
                break
            
    elif(InputMenu == 2):
        PrintItem(ListItem)
        AddItem()
    elif(InputMenu == 3):
        PrintItem(ListItem)
        InputID = input('Masukkan ID Item yang ingin di delete: ')
        DeleteItem(ListItem, InputID)
    elif(InputMenu == 4):
        PrintItem(ListItem)
        UpdateItem()
    elif(InputMenu == 5):
        break

    