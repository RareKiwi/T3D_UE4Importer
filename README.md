![](https://imgur.com/uxXfo56.png)

# &middot; T3D UE4Importer &middot;


T3D UE4Importer is a collection of UE4 Editor Utility widgets that can be used to simplify the process of converting Unreal Engine 2 levels and the needed referenced assets to Unreal Engine 4.27

## Expectations:

- Static Meshes imported and placed in level
   - Materials and textures assigned in bulk.
- Lights imported
   - Approximate conversion of settings to match old light rendering
- Other actors imported as text actors
   - Paramaters from .T3D added as actor tags
- Brush import
   - Bulk import of materials and textures referenced.
   - Materials assigned to surfaces.
   > Brush UVs are misaligned, but can be mostly resolved by setting scale to 2.56 x 2.56

## Download:

Use __*[Code > Download ZIP](../../archive/refs/heads/main.zip)*__

## [Install:](../../wiki/Install)

Place loose files somewhere in your projects __*`/Content/`*__

> Example: `/Content/T3D_UE4Importer/`

> Requires the engine plugin __*Editor Scripting Utilities*__ & __*UE4.27*__  
[Victory Plugin](https://forums.unrealengine.com/t/39-ramas-extra-blueprint-nodes-for-you-as-a-plugin-no-c-required/3448) is needed but the main widget can be modified to not need it. The ImporterFBX widget requires the plugin to function.


## Used Software:

[UE4-T3DConverter](https://forums.unrealengine.com/t/tool-ue4-t3d-converter-for-bsp-brushes/4057)([Mirror](https://drive.google.com/uc?id=1JA8__aWtyCOZEmQXkwmSCT_SESt6y0At&export=download))  
[UE Viewer](https://www.gildor.org/en/projects/umodel#files)  
[Victory Plugin](https://forums.unrealengine.com/t/39-ramas-extra-blueprint-nodes-for-you-as-a-plugin-no-c-required/3448)([4.27 Direct Link](https://www.mediafire.com/file/1snjjuxuoqs6b4g/VictoryPlugin27.zip/file))  
[Blender](https://www.blender.org/download/) and [Blender PSK plugin](https://github.com/matyalatte/blender3d_import_psk_psa/releases)

## Usage:

[Usage Tutorial](../../wiki/Usage-Tutorial)

## Images:

![Stormtroopocat](https://imgur.com/g5rgkG6.png "EUW_T3D_ActorImporter") ![Stormtroopocat](https://imgur.com/pA5uREG.png "EUW_LightHelper") ![Stormtroopocat](https://imgur.com/Vf9AKkZ.png "EUW_ImportFBX")
