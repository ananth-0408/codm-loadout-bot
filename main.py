import discord
import os

client = discord.Client()

@client.event 
async def on_ready() :
  print('Bot {0.user} is ready to destroy flag!'.format(client))
  await client.change_presence(activity=discord.Game(name="blem > sweg"))  
  
@client.event 
async def on_message(message) :
  if message.author == client.user :
    return

  if '$help' in message.content.lower() or if client.user.mentioned_in(message) :
    await message.reply('Please type `$loadout` followed by a space and the name of the gun for which you want the loadout. For example, `$loadout ak117`')

  if message.content.lower() == '$loadout' :
    await message.reply('You have to specify which gun you want the loadout for, smarty pants')

  if '$loadout bk57' in message.content.lower() :
    await message.reply('**Muzzle** : *MIP light flash guard* \n**Barrel** : *MIP Light Barrel(Short)* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Tactical Foregrip A* \n**Rear grip** : *Granulated grip tape* \n \nnoob')

  if '$loadout man-o-war' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Ranger* \n**Stock** : *MIP Light Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Tactical Foregrip A* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout drh' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Ranger* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Ammunition** : *25 Round OTM Mag* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout asm10' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Ranger* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Ammunition** : *33 Round Extended Mag* \n**Perk** : *Sleight Of Hand* \n \nnoob')

  if '$loadout lk24' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Integral Suppressor Light* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip A* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout ak117' in message.content.lower() :
    await message.reply('**Muzzle** : *Monolithic Suppressor* \n**Barrel** : *OWC Marksman* \n**Ammunition** : *48 Round Extended Mag* \n**Underbarrel** : *Ranger Foregrip A* \n**Laser** : *OWC Laser - Tactical* \n \nnoob')

  if '$loadout hvk30' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Light Barrel* \n**Stock** : *MIP Strike Stock* \n**Ammunition** : *Light Caliber Ammo* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Rubberized Grip Tape* \n \nnoob')

  if '$loadout as val' in message.content.lower() :
    await message.reply('**Barrel** : *VLK 200mm OSA* \n**Stock** : *FFS Intl. Gen 4 GRU* \n**Laser** : *Tac Laser* \n**Underbarrel** : *Merc Foregrip A* \n**Ammunition** : *30 round mag* \n \nnoob')
  
  if '$loadout hbra3' in message.content.lower() :
    await message.reply('**Muzzle** : *Monolithic Suppressor* \n**Optic** : *Classic Red Dot* \n**Laser** : *OWC Laser - Tactical* \n**Barrel** : *OWC Marksman* \n**Ammunition** : *44 round extended mag* \n \nnoob')

  if '$loadout kn44' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Muzzle** : *OWC Light Compensator* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout dlq33' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Light Barrel* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Bipod* \n**Perk** : *Sleight of Hand* \n \nnoob')

  if '$loadout msmc' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Muzzle** : *RTC Muzzle Break* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout s36' in message.content.lower() :
    await message.reply('**Optic** : *Red Dot Sight (not if you\'re a pay to win loser)* \n**Stock** : *YKM Light Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout type25' in message.content.lower() or '$loadout type 25' in message.content.lower() :
    await message.reply('**Ammunition** : *Stopping Power Reload* \n**Stock** : *RTC Steady Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout ak47' in message.content.lower() :
    await message.reply('**Barrel** : *MIP OWC Marksman* \n**Muzzle** : *RTC Light Muzzle Break* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Ranger Foregrip* \n**Stock** : *MIP Strike Stock* \n \nnoob')

  if '$loadout locus' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Lightweight Short* \n**Stock** : *OWC Skeleton Stock* \n**Laser** : *OWC Laser - Tactical* \n**Ammunition** : *Stopping Power Reload Foregrip* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout pdw' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Perk** : *Sleight of Hand* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser Tactical* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout razorback' in message.content.lower() :
    await message.reply('**Muzzle** : *OWC Light Compensator* \n**Underbarrel** : *Merc Foregrip* \n**Stock** : *MIP Strike Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout qq9' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Recon Tac Long* \n**Ammunition** : *45 Round Extended Mag* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser Tactical* \n**Underbarrel** : *Operator Foregrip* \n \nnoob')

  if '$loadout pharo' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Ammunition** : *44 Round Extended Mag* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout icr1' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Integral Suppressor Light* \n**Ammunition** : *40 Round Fast Reload* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout m4' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Ranger* \n**Muzzle** : *OWC Light Compensator Round Fast Reload* \n**Stock** : *MIP Strike Stock* \n**Laser** : *MIP Laser 5mW* \n**Underbarrel** : *Ranger Foregrip* \n \nnoob')

  if '$loadout by15' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Extended Light Barrel* \n**Muzzle** : *Marauder Suppressor* \n**Stock** : *OWC Ranger Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout ul736' in message.content.lower() :
    await message.reply('**Optic** : *Classic Red Dot Sight* \n**Ammunition** : *50 Round Reload* \n**Stock** : *YKM Light Stock* \n**Underbarrel** : *Strike Foregrip* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout outlaw' in message.content.lower() :
    await message.reply('**Barrel** : * MIP Memorial Cowboy* \n**Perk** : *FMJ* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Stripplrd Grip Tape* \n \nnoob')

  if '$loadout m16' in message.content.lower() :
    await message.reply('**UnderBarrel** : *Operator Foregrip* \n**Muzzle** : *OWC Light Compensator* \n**Stock** : *MIP Strike Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Rubberized Grip Tape* \n \nnoob')

  if '$loadout m4lmg' in message.content.lower() :
    await message.reply('**Optic** : *Classic Red Dot Sight* \n**Muzzle** : *RTC Light Muzzle Break* \n**Underbarrel** : *Operator Foregrip* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Rubberized Grip Tape* \n \nnoob')

  if '$loadout gks' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Integral Suppressor* \n**Ammunition** : *32 Round Fast Reload* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout hg40' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Muzzle** : *RTC Light Muzzle Brake* \n**Ammunition** : *40 Round Fast Reload* \n**Perk** : *Sleight Of Hand* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout m21ebr' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Steady* \n**Muzzle** : *Monolithic Suppressor* \n**Stock** : *MIP Strike Stock* \n**Ammunition** : *20 Round Reload* \n**Underbarrel** : *Strike Foregrip* \n \nnoob')

  if '$loadout xpr' in message.content.lower() :
    await message.reply('**Barrel** : *RTC CQB* \n**Ammunition** : *OWC Stopping Power Reload* \n**Stock** : *YKM Ghost Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Operator Foregrip* \n \nnoob')

  if '$loadout striker' in message.content.lower() :
    await message.reply('**Barrel** : *Light Barrel (Short)* \n**Muzzle** : *Choke* \n**Perk** : *Sleight of Hand* \n**Laser** : *MIP Laser 5mW* \n**Ammunition** : *Fast Reload Reload Case* \n \nnoob')

  if '$loadout striker' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Light* \n**Underbarrel** : *Strike Foregrip* \n**Stock** : *YKM Combat Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout hs0405' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Extended Light Barrel* \n**Muzzle** : *Choke* \n**Stock** : *No Stock* \n**Laser** : *MIP Laser 5mW* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout hs2126' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Heavy Barrel* \n**Muzzle** : *Choke* \n**Stock** : *YKM Light Stock* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Strike Foregrip* \n \nnoob')

  if '$loadout mx9' in message.content.lower() :
    await message.reply('stop using meta smh')

  if '$loadout holger' in message.content.lower() :
    await message.reply('stop using meta smh')  

  if '$loadout m13' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Silencer Barrel* \n**Ammunition** : *Large Extended Mag B* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout chopper' in message.content.lower() :
    await message.reply('stop using meta smh')

  if '$loadout rus79u' in message.content.lower() :
    await message.reply('**Barrel** : *YKM Integral Suppressor Light* \n**Ammunition** : *50 Round Extended Mag* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')
  
  if '$loadout fennec' in message.content.lower() :
    await message.reply('**Underbarrel** : *Operator Foregrip* \n**Muzzle** : *Monolithic Suppressor* \n**Stock** : *No Stock* \n**Laser** : *MIP Laser 5mW* \n**Ammunition** : *Extended Mag A* \n \nnoob')

  if '$loadout spr' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Light Monolithic Silencer Barrel* \n**Muzzle** : *Monolithic Suppressor* \n**Stock** : *OWC Skeleton Stock* \n**Laser** : *OWC Laser - Tactical* \n**Bolt** : *Light Bolt* \n \nnoob')

  if '$loadout rytec' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Light Barrel (Short)* \n**Perk** : *Full Ammo* \n**Stock** : *OWC Skeleton Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Strippled Grip Tape* \n \nnoob')

  if '$loadout krm' in message.content.lower() :
    await message.reply('**Barrel** : *RTC Extended Light Barrel* \n**Perk** : *Speed Up Kill* \n**Stock** : *No Stock* \n**Laser** : *MIP Laser 5mW* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout chopper' in message.content.lower() :
    await message.reply('stop using meta smh')

  if '$loadout r90' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Extended Light Barrel* \n**Muzzle** : *Choke* \n**Smoothbore** : *MFT Ultra Light Smoothbore* \n**Laser** : *OWC Laser - Tactical* \n**Underbarrel** : *Operator Foregrip* \n \nnoob')

  if '$loadout hades' in message.content.lower() :
    await message.reply('stop spamming this gun <:elmo:902126371109732353>')

  if '$loadout sks' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Light Barrel* \n**Ammunition** : *30 Round Extended Mag* \n**Stock** : *No Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout qxr' in message.content.lower() :
    await message.reply('**Barrel** : *OWC Marksman* \n**Muzzle** : *RTC Light Muzzle Break* \n**Underbarrel** : *Strike Foregrip* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout cr56 amax' in message.content.lower() :
    await message.reply('**Barrel** : *Intruder Stock* \n**Ammunition** : *Extended Mag A* \n**Muzzle** : *Monolithic Suppressor* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout peacekeeper' in message.content.lower() :
    await message.reply('**Barrel** : *Taskforce Barrel* \n**Ammunition** : *Double Stack Mag* \n**Underbarrel** : *Field Agent Foregrip* \n**Laser** : *Aim Assist Laser* \n**Rear Grip** : *Firm Grip Tape* \n \nnoob')

  if '$loadout peacemaker' in message.content.lower() :
    await message.reply('its peacekeeper not peacemaker lmao')

  if '$loadout arctic' in message.content.lower() :
    await message.reply('***Warning*** : Low mobility lol its gonna make you puke \n**Barrel** : *Anti Material Heavy* \n**Muzzle** : *RTC Compensator* \n**Stock** : *RTC Steady Stock* \n**Underbarrel** : *Bipod* \n**Ammunition** : *MIP Stopping Power Reload* \n \nsuffer')

  if '$loadout fr' in message.content.lower() :
    await message.reply('**Muzzle** : *Monolithic Suppressor* \n**Barrel** : *OWC Ranger* \n**Stock** : *RTC Steady Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout mk2' in message.content.lower() :
    await message.reply('**Barrel** : *18.0 Sport Barrel* \n**Ammunition** : *.30 - 30 Ammo* \n**Stock** : *Cartridge Sleeve* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Stippled Grip Tape* \n \nnoob')

  if '$loadout kilo' in message.content.lower() :
    await message.reply('**Barrel** : *MIP Extended Light Barrel* \n**Ammunition** : *OWC Stopping Power Reload* \n**Stock** : *RTC Steady Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Stippled Grip Tape* \n \nnoob')

  if '$loadout echo' in message.content.lower() :
    await message.reply('nah you aint spamming it today noob')

  if '$loadout rpd' in message.content.lower() :
    await message.reply('stop spamming this gun <:elmo:902126371109732353>')

  if '$loadout cordite' in message.content.lower() :
    await message.reply('**Muzzle** : *Monolithic Suppressor* \n**Ammunition** : *80 Round Extended Mag* \n**Stock** : *MIP Strike Stock* \n**Laser** : *OWC Laser - Tactical* \n**Rear Grip** : *Granulated Grip Tape* \n \nnoob')

  if '$loadout na' in message.content.lower() :
    await message.reply('NOOOOOOOOOOOOOOOOOOOO :rage:')

  
  

client.run(os.getenv('TOKEN'))
