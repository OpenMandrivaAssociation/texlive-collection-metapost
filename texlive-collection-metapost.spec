# revision 23252
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-metapost
Epoch:		1
Version:	20120224
Release:	1
Summary:	MetaPost (and Metafont) drawing packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-metapost.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-automata
Requires:	texlive-bbcard
Requires:	texlive-blockdraw_mp
Requires:	texlive-bpolynomial
Requires:	texlive-cmarrows
Requires:	texlive-drv
Requires:	texlive-dviincl
Requires:	texlive-emp
Requires:	texlive-epsincl
Requires:	texlive-expressg
Requires:	texlive-exteps
Requires:	texlive-featpost
Requires:	texlive-feynmf
Requires:	texlive-garrigues
Requires:	texlive-gmp
Requires:	texlive-hatching
Requires:	texlive-latexmp
Requires:	texlive-metago
Requires:	texlive-metaobj
Requires:	texlive-metaplot
Requires:	texlive-metapost
Requires:	texlive-metauml
Requires:	texlive-mfpic
Requires:	texlive-mfpic4ode
Requires:	texlive-mp3d
Requires:	texlive-mpcolornames
Requires:	texlive-mpgraphics
Requires:	texlive-mpattern
Requires:	texlive-piechartmp
Requires:	texlive-roex
Requires:	texlive-slideshow
Requires:	texlive-splines
Requires:	texlive-suanpan
Requires:	texlive-textpath
Requires:	texlive-threeddice
Requires:	texlive-collection-basic

%description
TeXLive collection-metapost package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
