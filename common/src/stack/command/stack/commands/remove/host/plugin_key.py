# $Id$
# 
# @rocks@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @rocks@
#
# $Log$
# Revision 1.2  2010/09/07 23:52:57  bruno
# star power for gb
#
# Revision 1.1  2010/06/15 19:35:43  bruno
# commands to:
#  - manage public keys
#  - start/stop a service
#
#

import stack.commands


class Plugin(stack.commands.Plugin):

	def provides(self):
		return 'key'

	def run(self, hosts):
		for host in hosts:
			self.owner.db.execute("""delete from public_keys where
				node = (select id from nodes where name = '%s') """ %
				(host))
