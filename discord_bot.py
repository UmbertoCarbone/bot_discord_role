# Librerie principali per il bot Discord
# Main libraries for the Discord bot
import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv
import os


# Carica le variabili d'ambiente dal file .env
# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Impostazioni degli intent per il bot (necessario per leggere i messaggi e i ruoli)
# Bot intents settings (needed to read messages and roles)
intents = discord.Intents.default()
intents.message_content = True

# Crea l'istanza del bot
# Create the bot instance
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)


# View con i bottoni per selezionare i ruoli
# View with buttons to select roles
class RuoliView(View):
    def __init__(self, member):
        super().__init__(timeout=None)
        # Lista dei ruoli disponibili (modifica qui i nomi dei ruoli Discord)
        # List of available roles (edit here the Discord role names)
        self.ruoli = [
            "Fungo 🍄",
            "Sailor Moon 🌙",
        ]
        member_roles = [role.name for role in member.roles]
        for ruolo in self.ruoli:
            # Se l'utente ha già il ruolo, il bottone è rosso e disabilitato
            # If the user already has the role, the button is red and disabled
            if ruolo in member_roles:
                style = discord.ButtonStyle.danger
                disabled = True
            else:
                # Altrimenti il bottone è verde e cliccabile
                # Otherwise the button is green and clickable
                style = discord.ButtonStyle.success
                disabled = False
            self.add_item(self.make_button(ruolo, style, disabled))

    # Crea un bottone per ogni ruolo
    # Create a button for each role
    def make_button(self, ruolo, style, disabled):
        async def callback(interaction: discord.Interaction):
            # Se il bottone è disabilitato, mostra solo un messaggio
            # If the button is disabled, just show a message
            if disabled:
                await interaction.response.send_message(
                    f"You already have the Discord role '{ruolo}'.", ephemeral=True
                )
                return
            member = interaction.user
            guild = interaction.guild
            discord_role = discord.utils.get(guild.roles, name=ruolo)
            if discord_role:
                try:
                    # Assegna il ruolo all'utente
                    # Assign the role to the user
                    await member.add_roles(discord_role)
                    await interaction.response.send_message(
                        f"You have received the Discord role '{ruolo}'!", ephemeral=True
                    )
                    # Recupera il membro aggiornato dal server (per aggiornare la view)
                    # Fetch the updated member from the server (to update the view)
                    member = await guild.fetch_member(member.id)
                except Exception as e:
                    await interaction.response.send_message(
                        f"I can't assign you the role '{ruolo}': {e}", ephemeral=True
                    )
            else:
                await interaction.response.send_message(
                    f"You selected the role '{ruolo}', but it does not exist as a Discord role!",
                    ephemeral=True,
                )
            # Aggiorna la view con i ruoli aggiornati
            # Update the view with the updated roles
            refreshed_view = RuoliView(member)
            await interaction.message.edit(view=refreshed_view)

        btn = Button(label=ruolo, style=style, custom_id=ruolo, disabled=disabled)
        btn.callback = callback
        return btn


# Evento quando il bot si connette
# Event when the bot connects
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")


# Comando per mostrare i bottoni dei ruoli
# Command to show the role buttons
@bot.command(name="role")
async def role(ctx):
    """Send the buttons to choose roles."""
    view = RuoliView(ctx.author)
    await ctx.send("Choose a role:", view=view)


# Comando di saluto
# Greeting command
@bot.command()
async def ciao(ctx):
    """Responds with a greeting."""
    await ctx.send("Hi! I am a Discord bot.")


# Avvia il bot usando il token dal file .env
# Start the bot using the token from the .env file
bot.run(TOKEN)
