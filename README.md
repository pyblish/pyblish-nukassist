### ![](https://cloud.githubusercontent.com/assets/2152766/6998101/5c13946c-dbcd-11e4-968b-b357b7c60a06.png)

Pyblish integration for The Foundry NukeAssist.

<br>
<br>
<br>

### What is included?

A set of common plug-ins and functions shared across other integrations - such as getting the current working file. It also visually integrates Pyblish into the File-menu for easy access.

- Common [plug-ins](https://github.com/pyblish/pyblish-nukeassist/tree/master/pyblish_nukeassist/plugins)
- Common [functionality](https://github.com/pyblish/pyblish-nukeassist/blob/master/pyblish_nukeassist/__init__.py)
- File-menu shortcut

<br>
<br>
<br>

### Installation

pyblish-nukeassist depends on [pyblish-base](https://github.com/pyblish/pyblish-base) and is available via PyPI.

Ensure Pyblish for NukeAssist is on your `PYTHONPATH` and run this within NukeAssist.

```python
import pyblish_nukeassist
pyblish_nukeassist.setup()
```

You may also want to consider a graphical user interface, such as [pyblish-qml](https://github.com/pyblish/pyblish-qml) or [pyblish-lite](https://github.com/pyblish/pyblish-lite).
You can then show the Pyblish graphical user interface by calling `show()`.

```python
pyblish_nukeassist.show()
```

<br>
<br>
<br>

### Persistence

It is recommended that you allow Pyblish to load upon launching NukeAssist. For this, you have two options.

1. Add the following snippet to your `.nuke/menu.py` in your home directory:

  ```python
  # 1. Register your favourite GUI
  import pyblish.api
  pyblish.api.register_gui("pyblish_lite")

  # 2. Set-up Pyblish for NukeAssist
  import pyblish_nukeassist
  pyblish_nukeassist.setup()
  ```
2. Add the `pyblish_nukeassist/nuke_path` directory to your `NUKE_PATH` environment variable

As you will find, this directory contains a `menu.py` with the same command. Nuke will run this upon startup, along with any other `menu.py` available.

![](https://cloud.githubusercontent.com/assets/2152766/7269936/f64c8cc8-e8cf-11e4-9550-6d3c70ce6b02.png)

<br>
<br>
<br>

### Documentation

- [Under the hood](#under-the-hood)
- [Manually show GUI](#manually-show-gui)
- [No menu-item](#no-menu-item)
- [Teardown pyblish-nuke](#teardown-pyblish-nuke)
- [No GUI](#no-gui)
- [Environment Variables](#environment-variables)

<br>
<br>
<br>

##### Under the hood

The `setup()` command will:

1. Register Nuke related ["hosts"](http://api.pyblish.com/pages/Plugin.hosts.html), allowing plug-ins to be filtered accordingly.
3. Register a minimal set of plug-ins that are common across all integrations.

<br>
<br>
<br>

##### Manually show GUI

The menu-button is set to run `show()`, which you may also manually call yourself, such as from a shelf-button.

```python
import pyblish_nukeassist
pyblish_nukeassist.show()
```

<br>
<br>
<br>

##### No menu-item

Should you not want a menu-item, pass `menu=False`.

```python
import pyblish_nukeassist
pyblish_nukeassist.show(menu=False)
```

<br>
<br>
<br>

##### Dockable GUI

Should you want to dock the pyblish UI, there is a convenience function to help.

```python
import pyblish_nukeassist
window = pyblish_nukeassist.show()
pyblish_nukeassist.dock(window)
```

<br>
<br>
<br>

##### Teardown pyblish-nukeassist

To get rid of the menu, and completely remove any trace of pyblish-nukeassist from your Nuke session, run `teardown()`.

```python
import pyblish_nukeassist
pyblish_nukeassist.teardown()
```

This will do the opposite of `setup()` and clean things up for you.

<br>
<br>
<br>

##### No GUI

In the event that no GUI is registered upon running `setup()`, the button will provide the *user* with this information on how they can get up and running on their own.

![image](https://cloud.githubusercontent.com/assets/2152766/16318872/d63b7f60-3988-11e6-9431-f64991aabef3.png)

![image](https://cloud.githubusercontent.com/assets/2152766/16318883/ddf159f0-3988-11e6-8ef5-af5fd8dde725.png)

![image](https://cloud.githubusercontent.com/assets/2152766/16318893/e7d4cc9a-3988-11e6-92e9-c16037e51fb7.png)

##### Environment Variables

You can customize the integration with these environment variables:

Environment Variable | Description | Examples
--- | --- | ---
```PYBLISH_HOTKEY``` | Hotkey for executing ```File > Publish```. The hotkey is not case-sensitive. You can read more about it [here](https://www.thefoundry.co.uk/products/nuke/developers/63/pythondevguide/custom_ui.html#assigning-a-hotkey). | ```ctrl+p```, ```Ctrl+Alt+P```, ```CTRL+SHIFT+P```
