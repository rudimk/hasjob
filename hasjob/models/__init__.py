# -*- coding: utf-8 -*-

from datetime import timedelta
from flask.ext.sqlalchemy import SQLAlchemy
from coaster import LabeledEnum
from coaster.sqlalchemy import BaseMixin, BaseNameMixin, TimestampMixin
from .. import app


db = SQLAlchemy(app)
agelimit = timedelta(days=30)
newlimit = timedelta(days=1)

webmail_domains = set([
    'aol.com',
    'anonymous.to',
    'comcast.net',
    'dispostable.com',
    'everymail.net',
    'everyone.net',
    'facebook.com',
    'fastmail.fm',
    'flashmail.com',
    'gmail.com',
    'gmx.com',
    'googlemail.com',
    'guerillamail.com',
    'hotmail.com',
    'hotmail.fr',
    'hotmail.it',
    'hushmail.com',
    'inbox.com',
    'live.com',
    'lycos.com',
    'mail.com',
    'mail.ru',
    'mailinator.com',
    'me.com',
    'msn.com',
    'onebox.com',
    'outlook.com',
    'pobox.com',
    'qmail.com',
    'rediff.com',
    'runbox.com',
    'seznam.cz',
    'spamgourmet.com',
    'trashmail.net',
    'yahoo.com',
    'yahoo.co.in',
    'yandex.ru',
    'ymail.com',
    'yopmail.com',
    'zoho.com',
    ])


class POSTSTATUS:
    DRAFT = 0         # Being written
    PENDING = 1       # Pending email verification
    CONFIRMED = 2     # Post is now live on site
    REVIEWED = 3      # Reviewed and cleared for push channels
    REJECTED = 4      # Reviewed and rejected as inappropriate
    WITHDRAWN = 5     # Withdrawn by owner
    FLAGGED = 6       # Flagged by users for review
    SPAM = 7          # Marked as spam
    MODERATED = 8     # Moderated, needs edit
    ANNOUNCEMENT = 9  # Special announcement

    UNPUBLISHED = (DRAFT, PENDING)
    GONE = (REJECTED, WITHDRAWN, SPAM)
    LISTED = (CONFIRMED, REVIEWED, ANNOUNCEMENT)
    POSTPENDING = (CONFIRMED, REVIEWED, REJECTED, WITHDRAWN, FLAGGED, SPAM, MODERATED, ANNOUNCEMENT)


class EMPLOYER_RESPONSE(LabeledEnum):
    NEW = (0, u"New")            # New application
    PENDING = (1, u"Pending")    # Employer viewed on website
    IGNORED = (2, u"Ignored")    # Dismissed as not worth responding to
    REPLIED = (3, u"Replied")    # Employer replied to candidate
    FLAGGED = (4, u"Flagged")    # Employer reported a spammer
    SPAM = (5, u"Spam")          # Admin marked this as spam
    REJECTED = (6, u"Rejected")  # Employer rejected candidate with a message


class PAY_TYPE(LabeledEnum):
    NOCASH    = (0, u"Nothing")
    ONETIME   = (1, u"One-time")
    RECURRING = (2, u"Recurring")


class CANDIDATE_FEEDBACK(LabeledEnum):
    NORESPONSE =     (0, u"No response")
    INPROCESS =      (1, u"In process")
    DID_NOT_GET =    (2, u"Did not get the job")
    DID_NOT_ACCEPT = (3, u"Got offer, did not accept")
    GOT_JOB =        (4, u"Got the job")


from .user import *
from .jobcategory import *
from .jobpostreport import *
from .jobtype import *
from .reportcode import *
from .jobpost import *
from .board import *
