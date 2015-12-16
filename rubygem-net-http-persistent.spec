%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global	gem_name	net-http-persistent

Summary:	Persistent connections using Net::HTTP plus a speed fix
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:	2.9.4
Release:	4%{?dist}
Group:		Development/Languages
License:	MIT

URL:		http://seattlerb.rubyforge.org/net-http-persistent
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:		rubygem-net-http-persistent-2.1-no-net-test.patch

%{?scl:BuildRequires: scldevel(ruby)}
BuildRequires:	%{?scl_prefix_ruby}ruby(release)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
BuildRequires:	%{?scl_prefix_ruby}rubygem(minitest)

Requires:	%{?scl_prefix_ruby}ruby(release)
Requires:	%{?scl_prefix_ruby}rubygems
BuildArch:	noarch

Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Persistent connections using Net::HTTP plus a speed fix for 1.8.  It's
thread-safe too.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description    doc
This package contains documentation for %{pkg_name}.


%prep
%setup -n %{pkg_name}-%{version} -q -c -T

mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

pushd .%{gem_instdir}
%patch0 -p1
popd

chmod 0644 ./%{gem_dir}/cache/%{gem_name}-%{version}.gem

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}/%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/{.autotest,.gemtest}

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:. -e 'Dir.glob("test/test_*.rb").each{|f| require f}'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/[A-Z]*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files	doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test/

%changelog
* Fri Jan 30 2015 Vít Ondruch <vondruch@redhat.com> - 2.9.4-4
- Make patch apply cleanly.

* Mon Jan 05 2015 Vít Ondruch <vondruch@redhat.com> - 2.9.4-3
- Update to net-http-persistent 2.9.4.

* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 2.8-3
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Thu Nov 28 2013 Josef Stribny <jstribny@redhat.com> - 2.8-2
- Get rid of patch leftovers

* Wed Nov 20 2013 Josef Stribny <jstribny@redhat.com> - 2.8-1
- Update to 2.8

* Thu May 30 2013 Josef Stribny <jstribny@redhat.com> - 2.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7-2
- Fix the tests patch to skip all tests needing net connection.

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.7-1
- Initial SCL package.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.1-3
- F-17: rebuild against ruby19

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.1-1
- 2.1

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0-1
- 2.0

* Sun Aug 14 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8.1-1
- 1.8.1

* Mon Jul  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.8-1
- 1.8

* Sun Apr 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.7-1
- 1.7

* Thu Mar 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6.1-1
- 1.6.1

* Thu Mar  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.6-1
- 1.6

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.2-1
- 1.5.2
- Patch0 merged

* Sat Feb 12 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.1-1
- 1.5.1

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-3
- Rescue the case where socket is Nil, for mechanize testsuite

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5-1
- 1.5

* Sun Jan 16 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1
- Initial package
