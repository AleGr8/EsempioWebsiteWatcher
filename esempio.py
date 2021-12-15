import requests
import time

# Programmino che cerca delle parole chiave nell'html di un sito e se trova corrispondenza manda un messggio al bot di telegram

def telegram_bot_sendtext(message):
    '''
    funzione che manda il messaggio al bot di telegram (copiata spudoratamente da internet)
    bot_token è il token del bot. Lo crei normalmente con BotFather
    bot_chatID il proprio chat id. puoi usare @get_id_bot per fartelo mandare
    '''

    bot_token = '' #es 5077398858:AAjctowncjgnekcjgja_34_Bnioeragewrgg
    bot_chatID = '' # es 123456789
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)

    return response.json() #esito dell'operazione..vabbè sarebbe meglio controllare per assicurarsi che non ci siano errori

def check_website():
    '''
    funzione che cerca una/più parole chiavi (Disponibile, aggiungi al carrello etc) nell'html di una pagina
    se c'è corrispondenza ritorna true, senno false
    '''

    url = 'https://www.unieuro.it/online/Smartphone/SM-A127FZKVEUE-pidSAMA1264NEW'
    r = requests.get(url)
    textHtml=r.text #questa è la pagina html. NB controlla che sia quella giusta. con unieuro dovrebbe esserlo, ma es amazon restituisce una pagina
                    # con un captcha da completare e non la pagina del prodotto...in quel caso boh ci sarà un altro metodo

    #dall'url della pagina cerco l'elemento che mi dice se un oggetto è disponibile o meno
    # questo è da vedere bene per evitare falsi positivi (prende il testo di un altro prodotto es tra i consigliati)
    #                                           negativi (c'è un altro messaggio che indica la disponibilità ma non lo controllo)
    startIndex=textHtml.find('Aggiungi al carrello')

    if startIndex==-1:
        return False
    
    return True
  
#-----------------------------------------------------------------------

intervalChecks=10 #ogni quanto fare un controllo sul sito. occhio che magari con intervalli troppo piccoli telegram ti rompe le balle, non so
intervalMessage=10#ogni quanto farsi mandare un messaggio su telegram...non implementato ma secondo me serve un thread che fa da timer per evitare 
                     # di ricevere troppi messaggi se intervalChecks è un valore basso

while True:

    if check_website():
        telegram_bot_sendtext("é disponibile veloceeeeeeeeeee")
    else:
        telegram_bot_sendtext("non disponibile :(") #questa parte meglio togliela..se non ce chissene frega, utile per i test

    time.sleep(intervalChecks)

# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)
