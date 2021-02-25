import requests
import discord
from discord.ext import commands
import asyncio
import json


bot = commands.Bot(command_prefix='#', case_insensitive=True)

@bot.command()
async def mask(ctx, id):
	try:
		url = "https://api.opensea.io/api/v1/assets"
		querystring = {"asset_contract_address":"0xc2c747e0f7004f9e8817db2ca4997657a7746928", "token_ids":"%s"%(str(id))}
		response = requests.request("GET", url, params=querystring)
		json_resp = json.loads(response.text)
		last_sale = json_resp["assets"][0]["last_sale"]
		embed = discord.Embed(title="HashMask id "+ str(id) + " " + json_resp["assets"][0]["name"], description="", color=0xf2ff00, inline=True)
		embed.set_image(url=json_resp["assets"][0]["image_thumbnail_url"])
		if last_sale is None:
			last_sale = "No informations found"
			embed.add_field(name="Last sale price", value=last_sale, inline = False)
		else:
			last_sale = json_resp["assets"][0]["last_sale"]["total_price"]
			last_sale = float(last_sale) / 1000000000000000000
			ticker = json_resp["assets"][0]["last_sale"]["payment_token"]["symbol"]
			embed.add_field(name="Last sale price", value=str(last_sale) +" "+ ticker, inline = False)
		embed.add_field(name="Owner username", value=json_resp["assets"][0]["owner"]["user"]["username"], inline = True)
		embed.add_field(name="Owner address", value=json_resp["assets"][0]["owner"]["address"], inline = True)
		embed.add_field(name="View on Opensea", value=json_resp["assets"][0]["permalink"], inline = False)
		await ctx.send(embed=embed)
	except:
		embed = discord.Embed(title="Error", description="Something wrong happened, try again! ", color=0xf2ff00)
		await ctx.send(embed=embed)

'''
@bot.command()
async def addr(ctx, addr):
        try:

		url = "https://api.opensea.io/api/v1/collections"

		querystring = {"offset":"0","limit":"300", "asset_owner":"0x4090b585c6ba6f8d8cbd76aa805f28069c732ca3"}

		response = requests.request("GET", url, params=querystring)

		
		json_resp = json.loads(response.text)
		print(json_resp)

	except:
		embed = discord.Embed(title="Error", description="Something wrong happened, try again! ", color=0xf2ff00)
		await ctx.send(embed=embed)
'''

bot.run("abcdefghi")
