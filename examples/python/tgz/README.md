tar.gz example service
----------------------
I'm a python service that is bundled into a gzipped tarball using setuptools `sdist`.

running the example
-------------------

Start the VM

```
$ vagrant up
```

Determine which port the VM is listening on for SSH:

```
$ vagrant ssh-config | grep Port
  Port 2202
```

Modify the `mendel.yml` `dev` port accordingly:

```
$ patch mendel.yml <<EOP
> 7c7
> <     port: 2200
> ---
> >     port: 2202
> EOP
```

Deploy to the VM:

```
$ mendel dev deploy
[127.0.0.1] Executing task 'deploy'
[localhost] local: python setup.py sdist

...

running sdist
running egg_info
writing requirements to myservice_app.egg-info/requires.txt

...

...

Successfully installed new release of myservice-app service
executing upstart:start
myservice-app start/running, process 4760
unable to track deployment event in graphite, no graphite host configured in ~/.mendel.conf
Unable to track deployment event in custom api, no api endpoint configured in ~/.mendel.conf

Done.
Disconnecting from 127.0.0.1:2200... done.
```

Test it out!

```
$ curl "http://127.0.0.1:8080"
Hello gregor. Hello Sprout #currently this might not work, but its likely a vagrant config issue, the app is running on the vagrant vm
```