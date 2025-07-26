# Guida passo-passo: Come implementare il bot Discord per la gestione dei ruoli

Questa guida ti accompagnerà nella creazione e nell'esecuzione di un bot Discord che permette agli utenti di assegnarsi ruoli tramite bottoni.

## 1. Crea un account Discord Developer e una nuova applicazione

1. Vai su [Discord Developer Portal](https://discord.com/developers/applications).
2. Accedi con il tuo account Discord.
3. Clicca su "New Application" e inserisci un nome per la tua applicazione (es. "Bot Ruoli").
4. Salva le modifiche.

## 2. Crea un Bot e copia il Token

1. Nella pagina della tua applicazione, vai nella sezione "Bot" (barra laterale sinistra).
2. Clicca su "Add Bot" e conferma.
3. (Opzionale) Personalizza nome e avatar del bot.
4. Clicca su "Reset Token" e poi su "Copy" per copiare il token del bot. **Salvalo in un posto sicuro!**

## 3. Invita il bot nel tuo server Discord

1. Vai su "OAuth2" > "URL Generator".
2. Seleziona "bot" tra gli scopes.
3. Nei "Bot Permissions" seleziona almeno:
   - Send Messages
   - Manage Roles
   - Read Messages/View Channels
4. Copia il link generato in basso e aprilo nel browser.
5. Seleziona il server dove vuoi aggiungere il bot e conferma.

## 4. Prepara l'ambiente di sviluppo

1. Assicurati di avere [Python 3.8+](https://www.python.org/downloads/) installato.
2. Installa le librerie necessarie aprendo il terminale nella cartella del progetto.
3. Apri il terminale e inserisci :
   ```
   pip install discord.py python-dotenv
   ```
4. Crea un file chiamato `.env` nella stessa cartella di `bot.py` e inserisci:
   ```env
   DISCORD_TOKEN=il_tuo_token_qui
   ```
   Sostituisci `il_tuo_token_qui` con il token copiato dal portale Discord Developer.

## 5. Configura i ruoli nel tuo server Discord

1. Vai nelle impostazioni del tuo server Discord.
2. Crea i ruoli che vuoi rendere selezionabili (es. "Fungo 🍄", "Sailor Moon 🌙").
3. Assicurati che il bot abbia il permesso di assegnare questi ruoli (il suo ruolo deve essere più in alto nella lista rispetto ai ruoli che assegna).

## 6. Avvia il bot

1. Assicurati che il file `bot.py` sia nella cartella del progetto.
2. Dal terminale, esegui:
   ```powershell
   python bot.py
   ```

> ℹ️ **Nota:**
> Questo bot funziona solo in locale, cioè rimane attivo solo mentre il file viene eseguito sul tuo computer.
> Se vuoi che il bot sia sempre online, dovrai ospitarlo su un server (ad esempio su un VPS, Heroku, Replit, ecc.).

3. Se tutto è corretto, vedrai nel terminale il messaggio di avvio del bot.

## 7. Usa il bot su Discord

- Nel canale dove il bot ha accesso, digita il comando:
  ```
  !role
  ```
- Il bot risponderà con i bottoni per selezionare i ruoli.
- Clicca su un bottone per ricevere il ruolo corrispondente.

---

**Nota:** Puoi modificare i nomi dei ruoli disponibili cambiando la lista `self.ruoli` nella classe `RuoliView` dentro `bot.py`.

Per problemi o domande, consulta la documentazione ufficiale di [discord.py](https://discordpy.readthedocs.io/) o chiedi supporto nella community Discord di Python Italia.
