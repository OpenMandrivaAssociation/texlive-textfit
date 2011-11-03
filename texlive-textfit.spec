# revision 20591
# category Package
# catalog-ctan /macros/latex/contrib/textfit
# catalog-date 2010-11-28 20:21:22 +0100
# catalog-license lppl1.3
# catalog-version 5
Name:		texlive-textfit
Version:	5
Release:	1
Summary:	Fit text to a desired size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textfit
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textfit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Package to fit text to a given width or height by scaling the
font. For example: \scaletowidth{3in}{This}. (The job is done
by calculating a magstep and applying it to the current font;
thus "This" will be very tall, as well as very wide; to scale
in just one dimension, use the facilities of the graphicx
package.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textfit/textfit.sty
%doc %{_texmfdistdir}/doc/latex/textfit/README
%doc %{_texmfdistdir}/doc/latex/textfit/makefile
%doc %{_texmfdistdir}/doc/latex/textfit/manifest
%doc %{_texmfdistdir}/doc/latex/textfit/textfit.pdf
#- source
%doc %{_texmfdistdir}/source/latex/textfit/textfit.dtx
%doc %{_texmfdistdir}/source/latex/textfit/textfit.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
