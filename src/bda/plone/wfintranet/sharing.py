from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from Products.CMFPlone import PloneMessageFactory as _

class LeaderRole(object):
   implements(ISharingPageRole)
   title = _(u"title_leads_workgroup", default=u"Leads workgroup")
   required_permission = 'Manage portal content'