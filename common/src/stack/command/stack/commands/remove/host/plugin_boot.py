# $Id$
# 
# @rocks@
# Copyright (c) 2000 - 2010 The Regents of the University of California
# All rights reserved. Rocks(r) v5.4 www.rocksclusters.org
# https://github.com/Teradata/stacki/blob/master/LICENSE-ROCKS.txt
# @rocks@
#
# $Log$
# Revision 1.5  2010/09/07 23:52:57  bruno
# star power for gb
#
# Revision 1.4  2009/05/01 19:07:00  mjk
# chimi con queso
#
# Revision 1.3  2009/04/23 17:12:29  bruno
# cleanup 'rocks remove host' command
#
# Revision 1.2  2009/03/13 22:19:56  mjk
# - route commands done
# - cleanup of stack.host plugins
#
# Revision 1.1  2008/12/15 22:27:21  bruno
# convert pxeboot and pxeaction tables to boot and bootaction tables.
#
# this enables merging the pxeaction and vm_profiles tables
#
# Revision 1.3  2008/10/18 00:55:55  mjk
# copyright 5.1
#
# Revision 1.2  2008/03/06 23:41:38  mjk
# copyright storm on
#
# Revision 1.1  2008/02/01 20:52:27  bruno
# use plugins to support removing all database entries for a host.
#
#

import stack.commands


class Plugin(stack.commands.Plugin):

	def provides(self):
		return 'boot'

	def run(self, hosts):
		self.owner.command('remove.host.boot', hosts)

