Name:           filotimo-backgrounds
Version:        0.4
Release:        1%{?dist}
Summary:        Wallpapers for Filotimo
License:        GPLv2+
URL:            https://github.com/filotimo-linux/filotimo-core-packages

Source0:        LICENSE

Source2:        CadinidiMisurina.jpg
Source4:        ColdDunes.jpg
Source5:        Dunes.jpg
Source8:        HillsandMountains.jpg
Source9:        InClouds.jpg
Source10:       Kiss.jpg
Source14:       Obelisk.jpg
Source15:       PassoGiau.jpg
Source18:       RaGusela.jpg
Source19:       Sand.jpg
Source21:       Wind.jpg

Source22:       COPYING
Source23:       metadata.json

BuildArch:     noarch
BuildRequires: ImageMagick
BuildRequires: zopfli
Requires:      filotimo-kde-overrides

Provides:      desktop-backgrounds-compat
Obsoletes:     desktop-backgrounds-compat

%description
Wallpapers for Filotimo.

%define debug_package %{nil}

%prep

%build

%install
install -pm 0644 %{SOURCE0} LICENSE

cd %{_sourcedir}

for file in $(ls | grep .jpg); do
    id=$(echo $file | cut -d '.' -f 1)

    mkdir -p %{buildroot}%{_datadir}/wallpapers/$id/contents/images
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/screenshot.jpg
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg
    cp metadata.json %{buildroot}%{_datadir}/wallpapers/$id/
    cp %{SOURCE22} %{buildroot}%{_datadir}/wallpapers/$id/

    sed -i 's/"@id@"/\"'"$id"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json

    name=""
    author_name=""
    author_email=""
    case "$id" in
        "ColdDunes")
        name="Cold Dunes"
        author_name="Marek Piwnicki"
        author_email="marpiwnicki@gmail.com"
        ;;
        "HillsandMountains")
        name="Hills and Mountains"
        author_name="Marek Piwnicki"
        author_email="marpiwnicki@gmail.com"
        ;;
        "InClouds")
        name="In Clouds"
        author_name="Marek Piwnicki"
        author_email="marpiwnicki@gmail.com"
        ;;
        "RaGusela")
        name="Ra Gusela"
        author_name="Eberhard Grossgasteiger"
        author_email="info@narrateography.art"
        ;;
        "PassoGiau")
        name="Passo Giau"
        author_name="Eberhard Grossgasteiger"
        author_email="info@narrateography.art"
        ;;
        "CadinidiMisurina")
        name="Cadini di Misurina"
        author_name="Eberhard Grossgasteiger"
        author_email="info@narrateography.art"
        ;;
        *)
        name=$id
        author_name="Marek Piwnicki"
        author_email="marpiwnicki@gmail.com"
        ;;
    esac
    sed -i 's/"@name@"/\"'"$name"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
    sed -i 's/"@author_name@"/\"'"$author_name"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
    sed -i 's/"@author_email@"/\"'"$author_email"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
done

mkdir -p %{buildroot}%{_datadir}/backgrounds/images
convert InClouds.jpg InClouds.png
cp InClouds.png %{buildroot}%{_datadir}/backgrounds/default.png
cp %{buildroot}%{_datadir}/backgrounds/default.png %{buildroot}%{_datadir}/backgrounds/default-dark.png
cp %{buildroot}%{_datadir}/backgrounds/default.png %{buildroot}%{_datadir}/backgrounds/images/default.png

%post


%files
%license LICENSE
%{_datadir}/wallpapers/*
%{_datadir}/backgrounds/default.png
%{_datadir}/backgrounds/default-dark.png
%dir %{_datadir}/backgrounds/images/
%{_datadir}/backgrounds/images/default*

%changelog
