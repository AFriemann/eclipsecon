# -*- coding: utf-8 -*-

import os
import click

from eclipsecon.config import load
from eclipsecon.youtube import Client as YouTubeClient


@click.group()
@click.option('-c', '--config', default=os.path.expanduser('~/.config/ec/config.json'))
@click.option('-t', '--token', envvar='EC_GOOGLE_TOKEN')
@click.pass_context
def root(ctx, config, token):
    ctx.obj = load(config)

    if token:
        ctx.obj.update(token=token)


@root.command('upload-recordings')
def upload_recordings():
    pass


@root.group()
def youtube():
    pass


@youtube.command()
@click.pass_context
def list(ctx):
    """ WE START HERE! """
    print('yay')

    print('my token', ctx.obj.get('token'))

    youtube = YouTubeClient(ctx.obj.get('token'))

    for video in youtube.list_liked_videos():
        print(video)

    print('nay')


#
