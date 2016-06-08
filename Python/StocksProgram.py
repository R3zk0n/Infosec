#Basic Stock v1 adding Gui soon.

import time
import urllib2
from urllib2 import urlopen
import os
# function calling yahoo Stocks.



sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']
sp500 = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp', 'adsk', 'adt', 'aee', 'aeo', 'aep', 'aes', 'aet', 'afl', 'agn', 'aig', 'aiv', 'aiz', 'akam', 'all', 'altr', 'alxn', 'amat', 'amd', 'amgn', 'amp', 'amt', 'amzn', 'an', 'anf', 'ann', 'aon', 'apa', 'apc', 'apd', 'aph', 'apol', 'arg', 'arna', 'aro', 'ati', 'atvi', 'avb', 'avp', 'avy', 'axp', 'azo', 'ba', 'bac', 'bax', 'bbby', 'bbry', 'bbt', 'bby', 'bcr', 'bdx', 'beam', 'ben', 'bf-b', 'bhi', 'big', 'biib', 'bk', 'bks', 'blk', 'bll', 'bmc', 'bms', 'bmy', 'brcm', 'brk-b', 'bsx', 'btu', 'bwa', 'bxp', 'c', 'ca', 'cab', 'cag', 'cah', 'cam', 'cat', 'cb', 'cbg', 'cbs', 'cce', 'cci', 'ccl', 'celg', 'cern', 'cf', 'cfn', 'chk', 'chrw', 'ci', 'cim', 'cinf', 'cl', 'clf', 'clx', 'cma', 'cmcsa', 'cme', 'cmg', 'cmi', 'cms', 'cnp', 'cnx', 'cof', 'cog', 'coh', 'col', 'cop', 'cost', 'cov', 'cpb', 'crm', 'csc', 'csco', 'csx', 'ctas', 'ctl', 'ctsh', 'ctxs', 'cvc', 'cvs', 'cvx', 'd', 'dal', 'dd', 'dds', 'de', 'dell', 'df', 'dfs', 'dg', 'dgx', 'dhi', 'dhr', 'dis', 'disca', 'dks', 'dlph', 'dltr', 'dlx', 'dnb', 'dnr', 'do', 'dov', 'dow', 'dps', 'dri', 'dsw', 'dte', 'dtv', 'duk', 'dva', 'dvn', 'ea', 'ebay', 'ecl', 'ed', 'efx', 'eix', 'el', 'emc', 'emn', 'emr', 'eog', 'eqr', 'eqt', 'esrx', 'esv', 'etfc', 'etn', 'etr', 'ew', 'exc', 'expd', 'expe', 'expr', 'f', 'fast', 'fb', 'fcx', 'fdo', 'fdx', 'fe', 'ffiv', 'fhn', 'fis', 'fisv', 'fitb', 'fl', 'flir', 'flr', 'fls', 'flws', 'fmc', 'fosl', 'frx', 'fslr', 'fti', 'ftr', 'gas', 'gci', 'gd', 'ge', 'ges', 'gild', 'gis', 'glw', 'gm', 'gmcr', 'gme', 'gnw', 'goog', 'gpc', 'gps', 'grmn', 'grpn', 'gs', 'gt', 'gww', 'hal', 'har', 'has', 'hban', 'hcbk', 'hcn', 'hcp', 'hd', 'hes', 'hig', 'hog', 'hon', 'hot', 'hov', 'hp', 'hpq', 'hrb', 'hrl', 'hrs', 'hsp', 'hst', 'hsy', 'hum', 'ibm', 'ice', 'iff', 'igt', 'intc', 'intu', 'ip', 'ipg', 'ir', 'irm', 'isrg', 'itw', 'ivz', 'jbl', 'jci', 'jcp', 'jdsu', 'jec', 'jnj', 'jnpr', 'josb', 'joy', 'jpm', 'jwn', 'k', 'key', 'kim', 'klac', 'kmb', 'kmi', 'kmx', 'ko', 'kr', 'krft', 'kss', 'ksu', 'l', 'leg', 'len', 'lh', 'life', 'lll', 'lltc', 'lly', 'lm', 'lmt', 'lnc', 'lo', 'low', 'lrcx', 'lsi', 'ltd', 'luk', 'luv', 'lyb', 'm', 'ma', 'mac', 'mar', 'mas', 'mat', 'mcd', 'mchp', 'mck', 'mco', 'mcp', 'mdlz', 'mdt', 'met', 'mgm', 'mhfi', 'mjn', 'mkc', 'mmc', 'mmm', 'mnst', 'mo', 'molx', 'mon', 'mos', 'mpc', 'mrk', 'mro', 'ms', 'msft', 'msi', 'mtb', 'mu', 'mur', 'mwv', 'myl', 'nbl', 'nbr', 'ndaq', 'ne', 'nee', 'nem', 'nflx', 'nfx', 'ni', 'nile', 'nke', 'nly', 'noc', 'nok', 'nov', 'nrg', 'nsc', 'ntap', 'ntri', 'ntrs', 'nu', 'nue', 'nvda', 'nwl', 'nwsa', 'nyx', 'oi', 'oke', 'omc', 'orcl', 'orly', 'oxy', 'p', 'payx', 'pbct', 'pbi', 'pcar', 'pcg', 'pcl', 'pcln', 'pcp', 'pdco', 'peg', 'pep', 'petm', 'pets', 'pfe', 'pfg', 'pg', 'pgr', 'ph', 'phm', 'pki', 'pld', 'pll', 'pm', 'pnc', 'pnr', 'pnw', 'pom', 'ppg', 'ppl', 'prgo', 'pru', 'psa', 'psx', 'pwr', 'px', 'pxd', 'qcom', 'qep', 'r', 'rai', 'rdc', 'rf', 'rhi', 'rht', 'rl', 'rok', 'rop', 'rost', 'rrc', 'rsg', 'rsh', 'rtn', 's', 'sai', 'sbux', 'scg', 'schl', 'schw', 'sd', 'se', 'see', 'sfly', 'shld', 'shw', 'sial', 'siri', 'sjm', 'sks', 'slb', 'slm', 'sna', 'sndk', 'sne', 'sni', 'so', 'spg', 'spls', 'srcl', 'sre', 'sti', 'stj', 'stt', 'stx', 'stz', 'swk', 'swn', 'swy', 'syk', 'symc', 'syy', 't', 'tap', 'tdc', 'te', 'teg', 'tel', 'ter', 'tgt', 'thc', 'tibx', 'tif', 'tjx', 'tm', 'tmk', 'tmo', 'trip', 'trow', 'trv', 'tsla', 'tsn', 'tso', 'tss', 'twc', 'twx', 'txn', 'txt', 'tyc', 'ua', 'unh', 'unm', 'unp', 'ups', 'urbn', 'usb', 'utx', 'v', 'vale', 'var', 'vfc', 'viab', 'vitc', 'vlo', 'vmc', 'vno', 'vprt', 'vrsn', 'vtr', 'vz', 'wag', 'wat', 'wdc', 'wec', 'wfc', 'wfm', 'whr', 'win', 'wlp', 'wm', 'wmb', 'wmt', 'wpo', 'wpx', 'wtw', 'wu', 'wy', 'wyn', 'wynn', 'x', 'xel', 'xl', 'xlnx', 'xom', 'xray', 'xrx', 'xyl', 'yhoo', 'yum', 'zion', 'zlc', 'zmh', 'znga', 'camp', 'cldx', 'ecyt', 'gtn', 'htz', 'nus', 'pvtb', 'qdel', 'snts', 'wgo', 'wwww']



timestmp = time.strftime("%Y\%m\%d")

timestmp2 = time.strftime("%Y\%m\%d Time : %-I:%-M:%S")
banner = '''\n================================================\n
                              	Stocks(PTBR) at %s\n
                  
            \n================================================\n''' % timestmp2




log ="file_%s" % timestmp

infofile = open(log, "w+")
infofile.write(banner)
User_input = input("Find PTB ratio: \n")
os.system('clear')
print "Please wait...\n"
def yahooKeyStats(stock):
	try:
		#Sourcing the info from Yahoo
		sourceCode = urllib2.urlopen('http://finance.yahoo.com.au/q/ks?s='+stock).read()
		pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
		PEG5 = sourceCode.split ('PEG Ratio (5 yr expected)<font size="-1"><sup>1</sup></font>:</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
		if float(pbr) < float(User_input):
			print "Stock:%s\n" % stock.upper()
			print "price to book ratio:\n",pbr
			infofile.write(str(stock.upper()+":"))
			infofile.write(str(pbr)+"\n")
			print "PEG5:%s\n" % PEG5
			infofile.write(str(PEG5)+"\n")

	# Except for error debugging
	except Exception,e:
		print "Failed in the main loop", str(e)





for eachStock in sp500short:
	
	yahooKeyStats(eachStock)
	
	time.sleep(1)
	
	
	

	