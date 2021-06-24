from discord.ext import commands

class Store(commands.Cog):
    """Commands for my personal Discord Games store.
    Will have around 200GB of games when complete."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def stickers(self, ctx):
        """Shows Sticker store pages
        Usage: "o.store stickers [stickerpack]"""
        await ctx.send(
            'To find the stickers currently avaliable in this store, type `o.help store stickers`. '
            'Please note: These pages will only work if you are in one of these following countries, '
            '`Canada`, `Brazil` or `Japan`.'
        )


    @commands.group(aliases=["servers"], invoke_without_command=True)
    async def invites(self, ctx):
        """Shows Game store invites
        Usage: "o.store invites|servers [servername]\""""
        await ctx.send(
            'These are games that do not have specific (linkable) store pages, '
            'so you will have to join the developers server to obtain the game. '
            'Use `o.help store invites` to see the applicable games.'
        )


    @commands.group(aliases=["games"], invoke_without_command=True)
    async def sku(self, ctx):
        """Shows Game store pages (SKU)
        Usage: "o.store sku|games [gamename]\""""
        await ctx.send(
            'These are games that have store pages that can be directly installed or visited. '
            'Most are free, but there are a few paid in the mix. Use `o.help store sku` for a list of games and price.'
        )


    @commands.group(invoke_without_command=True)
    async def extras(self, ctx):
        """Shows extra store pages
        Usage: "o.store extras [extra]\""""
        await ctx.send(
            'These are store pages that are either for jokes or do nothing. Use `o.help store extras` for a full list')


    @commands.group(invoke_without_command=True)
    async def dlc(self, ctx):
        """Shows DLC pages (needs Base Game)
        Usage: "o.store dlc [game]\""""
        await ctx.send(
            'These are store pages that are DLC (downloadable content) '
            'that are avaliable for discord games that we have in the other store commands. '
            'Use `o.help store dlc` for the list of games with DLC'
        )


    @stickers.command()
    async def whatsupwumpus(self, ctx):
        """What's Up Wumpus - £2.99"""
        await ctx.send('https://ptb.discord.com/store/skus/748286108348973106/what-s-up-wumpus-sticker-pack')


    @stickers.command()
    async def hellowumpus(self, ctx):
        """Hello Wumpus - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/749043407997108384/hello-wumpus-sticker-pack')


    @invites.command()
    async def patchquest(self, ctx):
        """Patch Quest server invite"""
        await ctx.send('Patch Quest (Public Beta) - Free')
        await ctx.send('https://discord.com/invite/pyF5jmP')


    @invites.command()
    async def cookiedragon(self, ctx):
        """Two Kinds Online server invite"""
        await ctx.send('Two Kinds Online (Alpha) - Free')
        await ctx.send('https://discord.gg/cookiedragon')


    @invites.command()
    async def cycle28(self, ctx):
        """Cycle 28 Invite"""
        await ctx.send('Cycle 28 - £0.99 (-50%)')
        await ctx.send('https://discord.gg/FpD4SuYeCm')


    @invites.command()
    async def staysafe(self, ctx):
        """Yellowcake Games Invite"""
        await ctx.send('Stay Safe - £2.99')
        await ctx.send('https://discord.gg/yellowcakegames')


    @invites.command()
    async def hexrunpro(self, ctx):
        """Hex! Run Pro Invite"""
        await ctx.send('Hex! Run Pro - £19.99')
        await ctx.send('https://discord.gg/S9yAhrJrDg')


    @extras.command()
    async def poggers(self, ctx):
        """Poggers"""
        await ctx.send('https://canary.discord.com/store/skus/692146322924372089/poggers')


    @extras.command()
    async def yoshi(self, ctx):
        """Yoshi game"""
        await ctx.send('https://ptb.discord.com/store/skus/710797635388178462/yoshi')


    @extras.command()
    async def wiilink24(self, ctx):
        """Installing WiiLink24"""
        await ctx.send('https://ptb.discord.com/store/skus/806878609302093866/installing-wiilink24')


    @extras.command()
    async def nitro(self, ctx):
        """Discord Nitro Classic"""
        await ctx.send('https://ptb.discord.com/store/skus/715629060331405382/nitro-classic')


    @extras.command()
    async def bge(self, ctx):
        """Best Game Ever"""
        await ctx.send('https://ptb.discord.com/store/skus/461618159171141643/best-game-ever')


    @sku.command()
    async def koth(self, ctx):
        """King of the Hat - £14.99"""
        await ctx.send('https://ptb.discord.com/store/skus/486981988109254667/king-of-the-hat')


    @sku.command()
    async def minionmasters(self, ctx):
        """Minion Masters - Free (DLC)"""
        await ctx.send('https://ptb.discord.com/store/skus/488607666231443456/minion-masters')


    @dlc.command()
    async def minionmasters(self, ctx):
        """Minion Masters DLC - `o.store sku minionmasters`"""
        await ctx.send(
            'https://ptb.discord.com/store/skus/742277397105213440/nightmares\n'
            'https://canary.discord.com/store/skus/515467071924994048/all-masters\n'
            'https://canary.discord.com/store/skus/491564667983101953/premium-upgrade\n'
            'https://canary.discord.com/store/skus/548071645265264650/voidborne-onslaught\n'
            'https://canary.discord.com/store/skus/639095281668849664/crystal-conquest'
        )
        await ctx.send(
            'https://canary.discord.com/store/skus/565546081975533578/accursed-army-pack\n'
            'https://canary.discord.com/store/skus/607929247578849283/might-of-the-slither-lords\n'
            'https://canary.discord.com/store/skus/678878135697145866/zealous-inferno\n'
            'https://canary.discord.com/store/skus/707885099101847622/charging-into-darkness'
        )


    @sku.command()
    async def cdreboot(self, ctx):
        """Cerpe Diem: Reboot - £4.99"""
        await ctx.send('https://canary.discord.com/store/skus/568922402390671360/carpe-diem-reboot')


    @sku.command()
    async def forsakenr(self, ctx):
        """Forsaken Remastered - £16.98"""
        await ctx.send('https://ptb.discord.com/store/skus/494870847777931268/forsaken-remastered')


    @sku.command()
    async def forager(self, ctx):
        """Forager - £14.99"""
        await ctx.send('https://ptb.discord.com/store/skus/530541618504269875/forager')


    @sku.command()
    async def staysafe(self, ctx):
        """Stay Safe - £2.99"""
        await ctx.send('https://ptb.discord.com/store/skus/431807599860514817/stay-safe')


    @sku.command()
    async def steelseraph(self, ctx):
        """Steel Seraph - £1.99 (-33%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555820631007035413/steel-seraph')


    @sku.command()
    async def tanglewood(self, ctx):
        """TANGLEWOOD® - £7.99 (-43%)"""
        await ctx.send('https://ptb.discord.com/store/skus/378315252749565952/tanglewood-r')


    @sku.command()
    async def temtem(self, ctx):
        """Temtem - £30.99"""
        await ctx.send('https://ptb.discord.com/store/skus/558547388583772201/temtem')


    @sku.command()
    async def thevagrant(self, ctx):
        """The Vagrant - £1.99 (-50%)"""
        await ctx.send('https://ptb.discord.com/store/skus/562121024993230868/the-vagrant')


    @sku.command()
    async def underonewing(self, ctx):
        """Under One Wing - £28.99"""
        await ctx.send('https://ptb.discord.com/store/skus/555856535327342592/under-one-wing')


    @sku.command()
    async def newtontree(self, ctx):
        """Newton and the Apple Tree - £38.99"""
        await ctx.send('https://ptb.discord.com/store/skus/555867662442430483/newton-and-the-apple-tree')


    @sku.command()
    async def zombsroyaleio(self, ctx):
        """ZombsRoyale.io - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/519338998791929866/zombsroyale-io')


    @sku.command()
    async def realmroyale(self, ctx):
        """Realm Royale - Free (DLC)"""
        await ctx.send('https://ptb.discord.com/store/skus/518088627234930688/realm-royale')


    @dlc.command()
    async def realmroyale(self, ctx):
        """Realm Royale DLC - `o.store sku realmroyale`"""
        await ctx.send(
            'https://canary.discord.com/store/skus/564916655285600266/realm-royale-bass-drop-bundle\n'
            'https://canary.discord.com/store/skus/595360871472168991/realm-royale-cute-but-deadly-pack'
        )


    @sku.command()
    async def paladins(self, ctx):
        """Paladins - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/528145079819436043/paladins')


    @sku.command()
    async def heartwoods(self, ctx):
        """Heart of the Woods - £10.25 (-32%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555830991168733204/heart-of-the-woods')


    @sku.command()
    async def amagicalgirl(self, ctx):
        """A Magical High School Girl - £4.67 (-53%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555812072969994260/a-magical-high-school-girl')


    @sku.command()
    async def warframe(self, ctx):
        """Warframe - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/494959992483348480/warframe')


    @sku.command()
    async def pickcrafter(self, ctx):
        """Pickcrafter - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/560643262424285194/pickcrafter')


    @sku.command()
    async def assitd(self, ctx):
        """AT SUNDOWN: Shots in the Dark - £11.24"""
        await ctx.send('https://ptb.discord.com/store/skus/487031053454802946/at-sundown-shots-in-the-dark')


    @sku.command()
    async def madmachines(self, ctx):
        """MAD MACHINES - £9.99"""
        await ctx.send('https://ptb.discord.com/store/skus/487272772393762826/mad-machines')


    @sku.command()
    async def avoidplus(self, ctx):
        """Avoid Premium - £5.99"""
        await ctx.send('https://ptb.discord.com/store/skus/586603437299597333/avoid-premium')


    @sku.command()
    async def scpsl(self, ctx):
        """SCP: Secret Laboratory - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/420676877766623232/scp-secret-laboratory')


    @sku.command()
    async def sandboxes(self, ctx):
        """SandBoxes - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/519249930611589141/sandboxes')


    @sku.command()
    async def forestir(self, ctx):
        """Forestir - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/554072621000556584/forestir')


    @sku.command()
    async def ihbad(self, ctx):
        """Its Hard Being A Dog - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/565994833953554432/it-s-hard-being-a-dog')


    @sku.command()
    async def avoid(self, ctx):
        """Avoid - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/601864041731719189/avoid')


    @sku.command()
    async def hagwwii(self, ctx):
        """Heroes & Generals WWII - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/550277544025522176/heroes-generals-wwii')


    @dlc.command()
    async def hagwwii(self, ctx):
        """Heroes & Generals WWII DLC - `o.store sku hagwwii`"""
        await ctx.send(
            'https://ptb.discord.com/store/skus/558205987434266625/1200-gold\n'
            'https://ptb.discord.com/store/skus/565438968167137280/2200-gold\n'
            'https://ptb.discord.com/store/skus/557535890285658122/4800-gold\n'
            'https://ptb.discord.com/store/skus/565441415270629376/13000-gold\n'
            'https://ptb.discord.com/store/skus/565460799355617289/30000-gold'
        )


    @sku.command()
    async def soma(self, ctx):
        """SOMA - £28.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489230107093893120/soma')


    @sku.command()
    async def bannersaga(self, ctx):
        """Banner Saga 3 - £23.99"""
        await ctx.send('https://ptb.discord.com/store/skus/472483394085715979/banner-saga-3')


    @sku.command()
    async def starsonata(self, ctx):
        """Star Sonata 2 - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/459415040227803141/star-sonata-2')


    @sku.command()
    async def taopepel(self, ctx):
        """The Adventures of PepeL - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/554072366213234729/the-adventures-of-pepel')


    @sku.command()
    async def jumplats(self, ctx):
        """Jumplats - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/618864578545319956/jumplats')


    @sku.command()
    async def lftb(self, ctx):
        """Light From The Butt - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/594073512906588179/light-from-the-butt')


    @sku.command()
    async def metald(self, ctx):
        """Metal's Dungeon - £1.99"""
        await ctx.send('https://ptb.discord.com/store/skus/557494559257526272/metal-s-dungeon')


    @sku.command()
    async def mofanima(self, ctx):
        """Masters of Anima - £19.98"""
        await ctx.send('https://ptb.discord.com/store/skus/492418279717994505/masters-of-anima')


    @sku.command()
    async def parkasaurus(self, ctx):
        """Parkasaurus - £19.99"""
        await ctx.send('https://ptb.discord.com/store/skus/508008071411400724/parkasaurus')


    @sku.command()
    async def sinnersfr(self, ctx):
        """Sinner: Sacrifice for Redemption - £18.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489184797936058380/sinner-sacrifice-for-redemption')


    @sku.command()
    async def subnautica(self, ctx):
        """Subnautica - £24.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489926636943441932/subnautica')


    @sku.command()
    async def poe2df(self, ctx):
        """Pillars of Eternity II: Deadfire - £48.99"""
        await ctx.send('https://ptb.discord.com/store/skus/466696214818193408/pillars-of-eternity-ii-deadfire')


    @sku.command()
    async def subnautica2(self, ctx):
        """Subnautica: Below Zero - £24.99"""
        await ctx.send('https://ptb.discord.com/store/skus/535869836748783616/subnautica-below-zero')


    @sku.command()
    async def callofc(self, ctx):
        """Call of Cthulu - £39.99"""
        await ctx.send('https://ptb.discord.com/store/skus/503982482664849408/call-of-cthulhu-r')


    @sku.command()
    async def amnesiatdd(self, ctx):
        """Amnesia: The Dark Descent - £19.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489229235509002261/amnesia-the-dark-descent')


    @sku.command()
    async def hexrun(self, ctx):
        """Hex! Run - £0.99 (-50%)"""
        await ctx.send('https://ptb.discord.com/store/skus/598419143661846528/hex-run')


def setup(bot):
    bot.add_cog(Store(bot))