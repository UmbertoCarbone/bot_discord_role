import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv
import os
from keep_alive import keep_alive 
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

class RuoliView(View):
    def __init__(self, member):
        super().__init__(timeout=None)
        self.ruoli = [
            "HTML & CSS 🖌️",
            "JavaScript 🟨",
            "Python 🐍",
            "Node.js 🟩",
            "MYSQL 🐬",
            "React ⚛️",
            "Bootstrap 🅱️",
            "Tailwind CSS 🌬️",
            "TypeScript 🟦",
            "PHP 🐘",
            "Java ☕",
        ]
        member_roles = [role.name for role in member.roles]
        for ruolo in self.ruoli:
            if ruolo in member_roles:
                style = discord.ButtonStyle.danger
                disabled = True
            else:
                style = discord.ButtonStyle.success
                disabled = False
            self.add_item(self.make_button(ruolo, style, disabled))

    def make_button(self, ruolo, style, disabled):
        async def callback(interaction: discord.Interaction):
            if disabled:
                await interaction.response.send_message(
                    f"Hai già il ruolo '{ruolo}'.", ephemeral=True
                )
                return
            member = interaction.user
            guild = interaction.guild
            if guild is None:
                await interaction.response.send_message(
                    "Errore: impossibile accedere al server.", ephemeral=True
                )
                return
            discord_role = discord.utils.get(guild.roles, name=ruolo)
            if discord_role:
                try:
                    await member.add_roles(discord_role)
                    await interaction.response.send_message(
                        f"Ti è stato assegnato il ruolo '{ruolo}'!", ephemeral=True
                    )
                    member = await guild.fetch_member(member.id)
                except discord.Forbidden:
                    await interaction.response.send_message(
                        f"Permessi insufficienti per assegnare il ruolo '{ruolo}'.", ephemeral=True
                    )
                except Exception as e:
                    await interaction.response.send_message(
                        f"Errore imprevisto: {e}", ephemeral=True
                    )
            else:
                await interaction.response.send_message(
                    f"Il ruolo '{ruolo}' non esiste nel server!", ephemeral=True
                )
            # Non aggiorniamo la view per evitare errori 404 sui messaggi ephemeral

        btn = Button(label=ruolo, style=style, custom_id=ruolo, disabled=disabled)
        btn.callback = callback
        return btn

class InsegnantiView(View):
    def __init__(self, member):
        super().__init__(timeout=None)
        self.ruoli = [
            "Teacher 🧑‍🏫",
            "Careers Advisor 🧑‍🎓",
            "Project Work 🗂️",
            "Tutor 🧑‍💼",
            "AI 🤖"
            
        ]
        member_roles = [role.name for role in member.roles]
        for ruolo in self.ruoli:
            if ruolo in member_roles:
                style = discord.ButtonStyle.danger
                disabled = True
            else:
                style = discord.ButtonStyle.success
                disabled = False
            self.add_item(self.make_button(ruolo, style, disabled))

    def make_button(self, ruolo, style, disabled):
        async def callback(interaction: discord.Interaction):
            if disabled:
                await interaction.response.send_message(
                    f"Hai già il ruolo '{ruolo}'.", ephemeral=True
                )
                return
            member = interaction.user
            guild = interaction.guild
            if guild is None:
                await interaction.response.send_message(
                    "Errore: impossibile accedere al server.", ephemeral=True
                )
                return
            discord_role = discord.utils.get(guild.roles, name=ruolo)
            if discord_role:
                try:
                    await member.add_roles(discord_role)
                    await interaction.response.send_message(
                        f"Ti è stato assegnato il ruolo '{ruolo}'!", ephemeral=True
                    )
                    member = await guild.fetch_member(member.id)
                except discord.Forbidden:
                    await interaction.response.send_message(
                        f"Permessi insufficienti per assegnare il ruolo '{ruolo}'.", ephemeral=True
                    )
                except Exception as e:
                    await interaction.response.send_message(
                        f"Errore imprevisto: {e}", ephemeral=True
                    )
            else:
                await interaction.response.send_message(
                    f"Il ruolo '{ruolo}' non esiste nel server!", ephemeral=True
                )
            # Non aggiorniamo la view per evitare errori 404 sui messaggi ephemeral

        btn = Button(label=ruolo, style=style, custom_id=ruolo, disabled=disabled)
        btn.callback = callback
        return btn

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

# Comando slash /role
@bot.tree.command(name="role", description="Scegli i tuoi ruoli Discord")
async def role_slash(interaction: discord.Interaction):
    if interaction.channel.name != "ruoli":
        await interaction.response.send_message(
            "⚠️ Questo comando può essere usato solo nel canale #ruoli!",
            ephemeral=True
        )
        return
    view = RuoliView(interaction.user)
    await interaction.response.send_message(
        "Scegli i tuoi ruoli:",
        view=view,
        ephemeral=True
    )

# Comando slash /roleinsegnanti
@bot.tree.command(name="roleinsegnanti", description="Scegli i tuoi ruoli insegnanti")
async def role_insegnanti_slash(interaction: discord.Interaction):
    if interaction.channel.name != "ruoli":
        await interaction.response.send_message(
            "⚠️ Questo comando può essere usato solo nel canale #ruoli!",
            ephemeral=True
        )
        return
    view = InsegnantiView(interaction.user)
    await interaction.response.send_message(
        "Scegli i tuoi ruoli insegnanti:",
        view=view,
        ephemeral=True
    )
# =========================
# Avvia keep_alive e il bot
# =========================
keep_alive()
bot.run(TOKEN)