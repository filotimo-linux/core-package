Name:           filotimo-backgrounds
Version:        0.2
Release:        1%{?dist}
Summary:        Wallpapers for Filotimo
License:        GPLv2+
URL:            https://github.com/filotimo-linux/filotimo-core-packages

Source0:        LICENSE
Source1:        ColdDunes.jpg
Source2:        Dunes.jpg
Source3:        HillsandMountains.jpg
Source4:        InClouds.jpg
Source5:        Kiss.jpg
Source6:        Obelisk.jpg
Source7:        Sand.jpg
Source8:        Sunrise.jpg
Source9:        Wind.jpg

Source21:       COPYING
Source22:       metadata.json

BuildArch:     noarch
BuildRequires: ImageMagick
Requires:      filotimo-kde-overrides


%description
Wallpapers for Filotimo.

%define debug_package %{nil}

%prep

%build

%install
install -pm 0644 %{SOURCE0} LICENSE

cd %{_sourcedir}

author_name="Marek Piwnicki"
author_email="marpiwnicki@gmail.com"

for file in $(ls | grep .jpg); do
    id=$(echo $file | cut -d '.' -f 1)

    mkdir -p %{buildroot}%{_datadir}/wallpapers/$id/contents/images
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/screenshot.jpg
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg
    magick %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).png
    rm -f %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg
    cp metadata.json %{buildroot}%{_datadir}/wallpapers/$id/
    cp %{SOURCE21} %{buildroot}%{_datadir}/wallpapers/$id/

    sed -i 's/"@id@"/\"'"$id"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json

    name=""
    case "$id" in
        "ColdDunes") name="Cold Dunes"
        ;;
        "HillsandMountains") name="Hills and Mountains"
        ;;
        "InClouds") name="In Clouds"
        ;;
        "Canyon") name=$id author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "MountainPeak") name="Mountain Peak" author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "GlacialHeight") name="Glacial Height" author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "Mesa") name=$id author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "GardenoftheGods") name="Garden of the Gods" author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "WhiteandRed") name="White and Red" author_name="Patrick Hendry" author_email="worldsbetweenlines@gmail.com"
        ;;
        "Lake") name=$id author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        "RaGusela") name="Ra Gusela" author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        "PassoGiau") name="Passo Giau" author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        "CadinidiMisurina") name="Cadini di Misurina" author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        "AVeryTallMountainWithABitOfSnowOnIt") name="A Very Tall Mountain With A Bit Of Snow On It" author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        "PastelSky") name="Pastel Sky" author_name="Eberhard Grossgasteiger" author_email="info@narrateography.art"
        ;;
        *) name=$id
        ;;
    esac
    sed -i 's/"@name@"/\"'"$name"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
    sed -i 's/"@author_name@"/\"'"$author_name"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
    sed -i 's/"@author_email@"/\"'"$author_email"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
done


%files
%license LICENSE
%{_datadir}/wallpapers/*

%changelog
